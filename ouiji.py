from discord.ext import commands
from game import Game
from player import Player
import discord
import asyncio
from random import randint

class Ouiji(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx: commands.Context, member: discord.Member = None):
        """Ping the user you want to duel!"""
        channel_id = ctx.channel.id
        # Checks to see if the pinged user is valid
        if member is None:
            await ctx.send("Usage: !play [ping person you want to duel]")
        # elif member == ctx.author:
            # await ctx.send("You can't duel against yourself!")
        elif member == self.bot.user:
            await ctx.send(f"I'd like to duel with you, but I can't. {str(discord.utils.get(self.bot.emojis, name='defeat'))}")
        elif member.bot:
            await ctx.send(f"Beep boop. Shouldn't you play against a real person?")
        else:
            # Checks to see if the opponent responded to the bot in the right channel
            def check(m):
                return m.channel.id == channel_id and m.author == member
            await ctx.send(f"{member.display_name}, would you like to duel with {ctx.author.display_name}? Say 'yes' to accept. Any other response will count as a decline.")
            response = await self.bot.wait_for('message', check=check)
            if response.content.lower() == "yes":
                await ctx.send("It's time to duel!")
                players = [Player(ctx.author), Player(member)]
                player_one = players[randint(0, 1)]
                player_two = players[1] if player_one == players[0] else players[0]
                await Game(self.bot, ctx.message.guild).play(ctx, player_one, player_two)
            else:
                await ctx.send("Duel declined.")
                return