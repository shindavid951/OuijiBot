import discord
import asyncio
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
            currentPlayer = [player_one, player_two][self.turn % 2]
            self.drawPhase(currentPlayer, True)
            self.mainPhase(currentPlayer)
            self.turn += 1
        self.combatPhase(currentPlayer)
        # Main gameplay loop
        while (not self.detect_win(player_one, player_two)):
            currentPlayer = [player_one, player_two][self.turn % 2]
            self.drawPhase(currentPlayer)
            self.mainPhase(currentPlayer)
            self.combatPhase(currentPlayer)
            self.turn += 1
    
    async def drawPhase(self, ctx: commands.Context, player: Player, firstTurn=False):
        if firstTurn:
            player.hand.append(Deck[0]())
            await ctx.send(f"{player.member.display_name}, choose your first Card (Say 1, 2, or 3):")
            def check(m):
                return m.channel.id == ctx.channel.id and m.author == player.member
            choice = await self.bot.wait_for('message', check=check)
            while choice not in [1, 2, 3]:
                ctx.send("Invalid choice. Please choose again.")
                choice = await self.bot.wait_for('message', check=check)
            player.hand.append(Deck[choice]())
            if self.turn % 2 == 0:
                for _ in range(3):
                    player.hand.append(Deck[randint(1, 48)]())
            else:
                player.hand.append(Deck[randint(1, 48)]())
        else:
            #TODO: implement the draw phase for after the first turn
            pass
    
    #TODO: Implement the main phase
    async def mainPhase(self, player: Player):
        pass
        
    #TODO: Implement the combat phase
    async def combatPhase(self):
        pass
        