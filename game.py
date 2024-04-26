import discord
import PIL.Image
from typing import List
from discord.ext import commands
from deck import Deck
from player import Player
from random import randint

class Game(object):
    def __init__(self, bot: commands.Bot, server: discord.Guild):
        self.bot = bot
        self.server = server
        self.turn = 0

    # TODO: Add conditions for having no available units to play
    async def detect_win(self, player_one: Player, player_two: Player):
        return any([card.stars == 3 for card in player_one.field]) or any([card.stars == 3 for card in player_two.field])

    async def play(self, ctx: commands.Context, player_one: Player, player_two: Player):
        for _ in range(2):
            current_player = [player_one, player_two][self.turn % 2]
            self.draw_phase(ctx, current_player, True)
            self.main_phase(current_player)
            self.turn += 1
        self.combat_phase()
        # Main gameplay loop
        while (not self.detect_win(player_one, player_two)):
            current_player = [player_one, player_two][self.turn % 2]
            self.draw_phase(ctx, current_player)
            self.main_phase(current_player)
            self.combat_phase()
            self.turn += 1
    
    async def draw_phase(self, ctx: commands.Context, player: Player, first_turn=False):
        if first_turn:
            player.hand.append(Deck.deck[0]())
            await ctx.send(f"{player.member.display_name}, choose your first Card (Say 1, 2, or 3):")
            self.show_cards(ctx, [Deck.deck[1], Deck.deck[2], Deck.deck[3]], self.turn, True)
            def check(m):
                return m.channel.id == ctx.channel.id and m.author == player.member
            choice = await self.bot.wait_for('message', check=check)
            while choice not in [1, 2, 3]:
                ctx.send("Invalid choice. Please choose again.")
                choice = await self.bot.wait_for('message', check=check)
            player.hand.append(Deck.deck[choice]())
            if self.turn % 2 == 0:
                for _ in range(3):
                    player.hand.append(Deck.deck[randint(1, 48)]())
            else:
                player.hand.append(Deck.deck[randint(1, 48)]())
        else:
            #TODO: implement the draw phase for after the first turn
            pass
    
    #TODO: Implement the main phase
    async def main_phase(self, player: Player):
        pass
        
    #TODO: Implement the combat phase
    async def combat_phase(self):
        pass
    
    async def show_cards(self, ctx: commands.Context, cards, turn, first_turn=False, hand=False, field=False):
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
            await ctx.send(file=discord.File(hand_fp))
            cards_fp.close()
        else:
            if turn % 2 == 0:
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