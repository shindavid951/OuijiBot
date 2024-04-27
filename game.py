import discord
import PIL.Image
from discord.ext import commands
from deck import Deck
from player import Player
from random import randint

class Game(object):
    def __init__(self, bot: commands.Bot, server: discord.Guild, player_one: Player, player_two: Player):
        self.bot = bot
        self.server = server
        self.turn = 0
        self.current_phase = ""
        self.player_one = player_one
        self.player_two = player_two
        self.current_player = None

    # TODO: Add conditions for having no available units to play
    def detect_win(self):
        return any([card.stars == 3 for card in self.player_one.field]) or any([card.stars == 3 for card in self.player_two.field])

    async def play(self, ctx: commands.Context):
        # Simulates the first turn of the game
        for _ in range(2):
            self.current_player = [self.player_one, self.player_two][self.turn % 2]
            await self.draw_phase(ctx, True)
            await self.main_phase()
            self.turn += 1
        self.combat_phase()
        # Main gameplay loop
        while (not self.detect_win(self.player_one, self.player_two)):
            self.current_player = [self.player_one, self.player_two][self.turn % 2]
            await self.draw_phase(ctx)
            await self.main_phase()
            await self.combat_phase()
            self.turn += 1
    
    async def draw_phase(self, ctx: commands.Context, first_turn=False):
        self.current_phase = "Draw"
        if first_turn:
            deck = Deck()
            self.current_player.hand.append(deck.deck[0]())
            # The current player gets to pick a card from either
            #   The Poisonous Magician
            #   The Lone High Priestess
            #   or The Vengeful Empress
            await ctx.send(f"{self.current_player.member.display_name}, choose your first Card (Say 1, 2, or 3):")
            await self.show_cards(ctx, [deck.deck[1], deck.deck[2], deck.deck[3]], True)
            def check(m):
                return m.channel.id == ctx.channel.id and m.author == self.current_player.member
            choice = await self.bot.wait_for('message', check=check)
            while int(choice.content) not in [1, 2, 3]:
                await ctx.send("Invalid choice. Please choose again.")
                choice = await self.bot.wait_for('message', check=check)
            self.current_player.hand.append(deck.deck[choice]())
            # If it's player one's turn, they draw 3 more cards in addition to the ones the Fool and the card they chose.
            if self.turn % 2 == 0:
                for _ in range(3):
                    self.current_player.hand.append(deck.deck[randint(1, len(deck.deck))]())
            # Else, player two just draws one card. Womp womp.
            else:
                self.current_player.hand.append(deck.deck[randint(1, len(deck.deck))]())
        else:
            deck = Deck()
            # The current player can choose to forego their draw in favor of drawing a Foolish Indecisive
            await ctx.send(f"{self.current_player.member.display_name}, would you like to forego your draw to draw a Foolish Indecisive? (yes/no)")
            # Checks to see if the response message was by the right person and in the right channel
            def check(m):
                return m.channel.id == ctx.channel.id and m.author == self.current_player.member
            fool_draw = await self.bot.wait_for('message', check=check)
            while fool_draw.content.lower() not in ["yes", "no"]:
                await ctx.send("Sorry, I didn't get that. Would you like to forego your draw to draw a Foolish Indecisive? (yes/no)")
            # Adds the Foolish Indecisive to the current player's hand and ends the draw phase.
            if fool_draw.content.lower() == "yes":
                self.current_player.hand.append(deck.deck[0]())
                self.show_cards(ctx, self.current_player.hand, False, True)
                return
            self.current_player.hand.append(deck.deck[randint(1, len(deck.deck))]())
        # The player did not spend spirits and did not forgo their draw, so the draw phase now ends
        return
    
    #TODO: Implement the main phase
    async def main_phase(self, player: Player):
        self.current_phase = "Main"
        
    #TODO: Implement the combat phase
    async def combat_phase(self):
        self.current_phase = "Combat"
    
    async def show_cards(self, ctx: commands.Context, cards, first_turn=False, hand=False, field=False):
        images = [PIL.Image.open(x().image) for x in cards]
        widths, heights = zip(*(i.size for i in images))
        total_width = sum(widths)
        max_height = max(heights)
        cards_image = PIL.Image.new("RGB", (total_width, max_height))
        x_offset = 0
        for im in images:
            cards_image.paste(im, (x_offset, 0))
            x_offset += im.size[0]
        if first_turn:
            cards_image.save("./hand_images/first_pick.png")
            cards_fp = open("./hand_images/first_pick.png", "rb")
            await ctx.send(file=discord.File(cards_fp))
            cards_fp.close()
        else:
            if self.current_player == self.player_one:
                if hand:
                    cards_image.save("./hand_images/player_one_hand.png")
                    hand_fp = open("./hand_images/player_one_hand.png", "rb")
                    await ctx.send(file=discord.File(hand_fp))
                    hand_fp.close()
                elif field:
                    cards_image.save("./hand_images/player_one_field.png")
                    field_fp = open("./hand_images/player_one_field.png", "rb")
                    await ctx.send(file=discord.File(field_fp))
                    field_fp.close()
            else:
                if hand:
                    cards_image.save("./hand_images/player_two_hand.png")
                    hand_fp = open("./hand_images/player_two_hand.png", "rb")
                    await ctx.send(file=discord.File(hand_fp))
                    hand_fp.close()
                elif field:
                    cards_image.save("./hand_images/player_two_field.png")
                    field_fp = open("./hand_images/player_two_field.png", "rb")
                    await ctx.send(file=discord.File(field_fp))
                    field_fp.close()

    # The current player can choose to spend 1 or 2 spirits during their draw or main phase in order to draw an additional 1 or 2 cards.
    @commands.command()
    async def spirits(self, ctx: commands.Context):
        if self.current_player.spirits > 0 and self.current_phase not in ["Draw", "Main"]:
            deck = Deck()
            ctx.send("Would you like to spend spirits to draw additional cards? (yes/no)")
            def check(m):
                if m.author != self.current_player.member:
                    ctx.send("It's not your turn yet!")
                    return
                return m.channel.id == ctx.channel.id and m.author == self.current_player.member
            additional_draw = await self.bot.wait_for('message', check=check)
            while additional_draw.content.lower() not in ["yes", "no"]:
                await ctx.send("Sorry, I didn't get that. Would you like to spend spirits to draw additional cards? (yes/no)")
            if additional_draw.content.lower() == "yes":
                ctx.send("How many spirits would you like to spend? (1 or 2)")
                spirits_spent = await self.bot.wait_for('message', check=check)
                while spirits_spent.content.lower() not in ["1", "2", "one", "two"]:
                    await ctx.send("Sorry, I didn't get that. How many spirits would you like to spend? (1 or 2)")
                # Subtracts the appropriate amount of spirits from the player's spirit count, 
                # draws the appropriate number of cards, and ends the draw phase.
                if spirits_spent.content.lower() in ["1", "one"]:
                    self.current_player.spirits -= 1
                    self.current_player.hand.append(deck.deck[randint(1, len(deck.deck))]())
                    return
                elif spirits_spent.content.lower() in ["2", "two"]:
                    self.current_player.spirits -= 2
                    for _ in range(2):
                        self.current_player.hand.append(deck.deck[randint(1, len(deck.deck))]())
                        return
        else:
            if self.current_phase not in ["Draw", "Main"]:
                ctx.send("You can't spend spirits right now.")
                return
            ctx.send("You don't have enough spirits to spend right now.")
            return