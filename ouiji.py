from discord.ext import commands
from game import Game
import asyncio
import discord

class Ouiji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def play(self, ctx, member: discord.Member = None):
        """Ping the user you want to duel!"""
        channel_id = ctx.channel.id
        if member is None:
            await ctx.send("Ping the person you wish to play against.")
        elif member == ctx.author:
            await ctx.send("You can't duel against yourself!")
        elif member == self.bot.user:
            await ctx.send(f"I'd like to duel with you, but I can't. {str(discord.utils.get(self.bot.emojis, name='defeat'))}")
        else:
            await ctx.send("It's time to duel!")
            await Game(self.bot, ctx.message.server).play(ctx, ctx.author, member)