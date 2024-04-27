from discord.ext import commands
from discord import app_commands
from game import Game
from player import Player
import discord
from random import randint
import json

with open("config.json", "r") as cfg:
    data = json.load(cfg)

class Ouiji(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="play", description="Play a game of Ou-i-ji against someone!")
    @app_commands.guilds(data["guild_id"])
    @app_commands.describe(opponent = "Who would you like to play against?")
    async def play(self, interaction: discord.Interaction, opponent: discord.Member):
        ctx : commands.Context = await self.bot.get_context(interaction)
        channel_id = interaction.channel_id
        # Checks to see if the given user is valid
        # elif member == ctx.author:
            # await ctx.send("You can't duel against yourself!")
        if opponent == self.bot.user:
            await interaction.response.send_message(f"I'd like to duel with you, but I can't. {str(discord.utils.get(self.bot.emojis, name='defeat'))}")
        elif opponent.bot:
            await interaction.response.send_message(f"Beep boop. Shouldn't you play against a real person?")
        else:
            # Checks to see if the opponent responded to the bot in the right channel
            def check(m):
                return m.channel.id == channel_id and m.author == opponent
            await interaction.response.defer()
            await interaction.followup.send(f"{opponent.display_name}, would you like to duel with {interaction.user.display_name}? Say 'yes' to accept. Any other response will count as a decline.")
            response = await self.bot.wait_for('message', check=check)
            if response.content.lower() == "yes":
                await interaction.followup.send("It's time to duel!")
                players = [Player(interaction.user), Player(opponent)]
                player_one = players[randint(0, 1)]
                player_two = players[1] if player_one == players[0] else players[0]
                game = Game(self.bot, interaction.guild, player_one, player_two)
                await self.bot.add_cog(game)
                await game.play(ctx)
            else:
                await interaction.followup.send("Duel declined.")
                return