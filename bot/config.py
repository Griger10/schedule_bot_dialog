from environs import Env
from dataclasses import dataclass


@dataclass
class Config:
    bot_token: str
    admins_ids: list


@dataclass
class DatabaseConfig:
    dsn: str
    is_echo: bool


async def load_config() -> Config:
    env = Env()
    env.read_env()
    bot_token = env("BOT_TOKEN")
    admin_ids = [int(i) for i in env.list('ADMIN_IDS') if i != '']
    return Config(bot_token=bot_token, admins_ids=admin_ids)


def load_database() -> DatabaseConfig:
    env = Env()
    env.read_env()
    dsn = env("DATABASE_DSN")
    return DatabaseConfig(dsn=dsn, is_echo=False)
