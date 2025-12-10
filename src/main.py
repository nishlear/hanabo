import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Alive! Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ Token not found! Check your .env file.")