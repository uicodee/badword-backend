import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties

from app.infrastructure.database.factory import make_connection_string, create_pool
from app.tgbot import handlers, middlewares, dialogs
from app.config import load_config

dp = Dispatcher()


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    config = load_config()
    bot = Bot(token=config.tgbot.token, default=DefaultBotProperties(parse_mode="HTML"))
    pool = create_pool(url=make_connection_string(config))
    middlewares.setup(dp, pool=pool)
    handlers.setup(dp)
    dialogs.setup(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
