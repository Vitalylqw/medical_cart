from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from src.bot.router import get_router
from src.core.config import load_config
from src.core.logging import setup_logging
from src.core.storage import Storage


async def main() -> None:
	"""Entrypoint for polling run."""
	setup_logging()
	config = load_config()

	bot = Bot(token=config.telegram_token, parse_mode=ParseMode.HTML)
	dp = Dispatcher(storage=MemoryStorage())
	dp.include_router(get_router(config=config))

	# Ensure storage and runtime dirs
	storage = Storage(config)
	storage.ensure_runtime_dirs()
	storage.init_db()

	# Minimal bot commands
	await bot.set_my_commands(
		[
			BotCommand(command="start", description="Начать"),
			BotCommand(command="help", description="Помощь"),
			BotCommand(command="settings", description="Настройки"),
		]
	)
	await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
	# Lazy import to run async main with Python 3.10+
	import asyncio

	asyncio.run(main())


