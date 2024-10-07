from bot.config.config import load_database
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


async def load_connection():
    database_config = load_database()
    engine = create_async_engine(url=database_config.dsn, echo=database_config.is_echo)
    session_maker = async_sessionmaker(engine, expire_on_commit=False)

    async with session_maker() as session:
        session = session
    return session
