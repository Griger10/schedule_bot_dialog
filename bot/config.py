from environs import Env
from dataclasses import dataclass


@dataclass
class Config:
    bot_token: str


async def load_config() -> Config:
    env = Env()
    env.read_env()
    bot_token = env("BOT_TOKEN")
    return Config(bot_token=bot_token)