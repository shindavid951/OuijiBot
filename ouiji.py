from discord.ext import commands
from game import Game
import asyncio
import discord
import sys
import PIL.Image

class Ouiji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def play(self, ctx, member: discord.Member = None):
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
        else:
            await ctx.send("It's time to duel!")
            await Game(self.bot, ctx.message.server).play(ctx, ctx.author, member)