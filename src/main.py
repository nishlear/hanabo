import discord
from discord.ext import commands
from loguru import logger
from config import Config
from database import setup_database

def validate_config():
    try:
        Config.validate()
    except ValueError as e:
        logger.error(e)
        exit(1)

if __name__ == '__main__':
    logger.add(f"logs/app.log", rotation="1 day", retention="7 days") 
    
    validate_config()

    # Setup
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def setup_hook():
        await setup_database(bot)
        await bot.load_extension('commands.chat')
        await bot.load_extension('slashes.chat')
        
        # bot.tree.clear_commands(guild=None)  # Clears global commands
        await bot.tree.sync()

    bot.run(Config.DISCORD_TOKEN)