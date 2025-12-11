import asyncpg
from loguru import logger
from config import Config

async def setup_database(bot):
    """Connect to database and create tables"""
    logger.info(f"Connecting to database {Config.DB_NAME}")
    
    bot.pool = await asyncpg.create_pool(
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        host=Config.DB_HOST
    )
    
    async with bot.pool.acquire() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS player_links (
                discord_id BIGINT PRIMARY KEY,
                riot_puuid TEXT NOT NULL,
                riot_game_name TEXT,
                riot_tag_line TEXT,
                region TEXT DEFAULT 'na1',
                linked_at TIMESTAMP DEFAULT NOW()
            );
        """)
    
    logger.info("Database connected and tables ensured.")