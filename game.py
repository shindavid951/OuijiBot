import discord
import asyncio
from discord.ext import commands
from deck import Deck

class Game(object):
    def __init__(self, bot=None, server=None):
        self.bot = bot
        self.server = server

    async def play(self, ctx, playerOne, playerTwo):
        pass