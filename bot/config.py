from environs import Env
from dataclasses import dataclass


@dataclass
class Config:
    bot_token: str


@dataclass
class DatabaseConfig:
    dsn: str
    is_echo: bool


async def load_config() -> Config:
    env = Env()
    env.read_env()
    bot_token = env("BOT_TOKEN")
    return Config(bot_token=bot_token)


async def load_database() -> DatabaseConfig:
    env = Env()
    env.read_env()
    dsn = env("DATABASE_DSN")
    return DatabaseConfig(dsn=dsn, is_echo=False)
