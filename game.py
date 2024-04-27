import discord
import PIL.Image
import json
from discord.ext import commands
from discord import app_commands
from deck import Deck
from player import Player
from random import randint

with open("config.json", "r") as cfg:
    data = json.load(cfg)

class Game(commands.Cog):
    def __init__(self, bot: commands.Bot, server: discord.Guild=None, player_one: Player=None, player_two: Player=None):
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
            await self.show_cards([deck.deck[1](), deck.deck[2](), deck.deck[3]()], ctx, None, True)
            def check(m):
                return m.channel.id == ctx.channel.id and m.author == self.current_player.member
            choice = await self.bot.wait_for('message', check=check)
            while int(choice.content) not in [1, 2, 3]:
                await ctx.send("Invalid choice. Please choose again.")
                choice = await self.bot.wait_for('message', check=check)
            self.current_player.hand.append(deck.deck[int(choice.content)]())
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
    
    async def show_cards(self, cards, ctx: commands.Context = None, interaction: discord.Interaction = None, first_turn=False, hand=False, field=False):
        images = [PIL.Image.open(x.image) for x in cards]
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
                    await interaction.response.send_message(file=discord.File(hand_fp), ephemeral=True)
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
                    await interaction.response.send_message(file=discord.File(hand_fp), ephemeral=True)
                    hand_fp.close()
                elif field:
                    cards_image.save("./hand_images/player_two_field.png")
                    field_fp = open("./hand_images/player_two_field.png", "rb")
                    await ctx.send(file=discord.File(field_fp))
                    field_fp.close()

    # The current player can choose to spend 1 or 2 spirits during their draw or main phase in order to draw an additional 1 or 2 cards.
    @app_commands.command(name="spend_spirits", description="Spend 1 or 2 spirits in exchange for drawing addtional cards.")
    @app_commands.guilds(data["guild_id"])
    @app_commands.describe(spirits = "How many spirits do you want to spend? (1 or 2)")
    async def spirits(self, interaction: discord.Interaction, spirits: int):
        if interaction.user != self.current_player.member:
            await interaction.response.defer()
            await interaction.followup.send("It's not your turn yet!")
            return
        if self.current_player.spirits > 0 and self.current_phase not in ["Draw", "Main"]:
            deck = Deck()
            # Subtracts the appropriate amount of spirits from the player's spirit count, 
            # draws the appropriate number of cards, and ends the draw phase.
            if spirits == 1:
                self.current_player.spirits -= 1
                self.current_player.hand.append(deck.deck[randint(1, len(deck.deck))]())
                return
            elif spirits == 2:
                self.current_player.spirits -= 2
                for _ in range(2):
                    self.current_player.hand.append(deck.deck[randint(1, len(deck.deck))]())
                    return
            else:
                await interaction.response.defer()
                await interaction.followup.send("Invalid number of spirits entered.")
                return
        else:
            if self.current_phase not in ["Draw", "Main"]:
                await interaction.response.defer()
                await interaction.followup.send("You can't spend spirits right now.")
                return
            await interaction.response.defer()
            await interaction.followup.send("You don't have enough spirits to spend right now.")
            return
        
    @app_commands.command(name="show_hand", description="Shows you your current hand")
    @app_commands.guilds(data["guild_id"])
    async def show_hand(self, interaction: discord.Interaction):
        if interaction.user == self.player_one.member:
            await self.show_cards(self.player_one.hand, interaction=interaction, hand=True)
        elif interaction.user == self.player_two.member:
            await self.show_cards(self.player_two.hand, interaction=interaction, hand=True)
        else:
            await interaction.response.defer()
            await interaction.followup.send("You aren't playing in this game!")
            return