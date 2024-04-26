from discord.ext import commands
from game import Game
from player import Player
import asyncio
import discord
import sys
import PIL.Image
from random import randint

class Ouiji(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx: commands.Context, member: discord.Member = None):
        """Ping the user you want to duel!"""
        channel_id = ctx.channel.id
        # Save for later
        """
        images = [PIL.Image.open(x) for x in ["./card_images/AssuredCancer.png", "./card_images/PoisonedAssuredCancer.png", "./card_images/DepressedAssuredCancer.png", "./card_images/ForgottenAssuredCancer.png"]]
        widths, heights = zip(*(i.size for i in images))
        total_width = sum(widths)
        max_height = max(heights)
        hand = PIL.Image.new("RGB", (total_width, max_height))
        x_offset = 0
        for im in images:
            hand.paste(im, (x_offset, 0))
            x_offset += im.size[0]
        hand.save("./card_images/hand.png")
        handFP = open("./card_images/hand.png", "rb")
        await ctx.send(file=discord.File(handFP))
        hand.close()
        """

        if member is None:
            await ctx.send("Ping the person you wish to play against.")
        elif member == ctx.author:
            await ctx.send("You can't duel against yourself!")
        elif member == self.bot.user:
            await ctx.send(f"I'd like to duel with you, but I can't. {str(discord.utils.get(self.bot.emojis, name='defeat'))}")
        elif member.bot:
            await ctx.send(f"Beep boop. Shouldn't you play against a real person?")
        else:
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