from discord.ext import commands
import discord
from discord import app_commands  # Add this import
from loguru import logger

class ChatCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="hello", description="vcl no biet hello")  # Changed from @commands.tree.command
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message('Hello, world!')
    
    @app_commands.command(name="ping", description="Check bot latency")  # Changed
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Pong! Latency: {round(self.bot.latency * 1000)}ms')
    
    @app_commands.command(name="echo", description="Repeat your message")  # Changed
    @app_commands.describe(message="The message to echo")  # Optional: Add descriptions for parameters
    async def echo(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(message)

async def setup(bot):
    logger.info('Loading slashes.chat extension')
    await bot.add_cog(ChatCommands(bot))