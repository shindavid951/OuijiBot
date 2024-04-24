from discord.ext import commands
from ouiji import Ouiji
import discord
import asyncio
BOT_TOKEN = "MTIzMjQ4NzM5NTkxMjU4MTE2MA.Giv5yy.iTrW_QKkfegWtOQzTDFQ659DuIK6qKYSpdh3-M"
BOT_ID = 1232487395912581160

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event 
async def on_ready():
    print(f"Logged in as {bot.user.name}")

async def main():
    async with bot:
        await bot.add_cog(Ouiji(bot))
        await bot.start(BOT_TOKEN)

asyncio.run(main())