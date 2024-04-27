from discord.ext import commands
from typing import Literal, Optional
from ouiji import Ouiji
from game import Game
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

@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")
asyncio.run(main())