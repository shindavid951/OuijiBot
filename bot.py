from discord.ext import commands
from ouiji import Ouiji
import discord
import asyncio
import json

with open("config.json", "r") as cfg:
    data = json.load(cfg)

BOT_TOKEN = data["token"]
BOT_ID = data["id"]

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event 
async def on_ready():
    print(f"Logged in as {bot.user.name}")

async def main():
    async with bot:
        await bot.add_cog(Ouiji(bot))
        await bot.start(BOT_TOKEN)

asyncio.run(main())