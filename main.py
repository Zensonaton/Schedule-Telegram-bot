# coding: utf-8

import asyncio

import aiogram
from loguru import logger

from bot import getTelegramBot

BOT, DP = getTelegramBot()

async def onBotStart(dp: aiogram.Dispatcher) -> None:
	"""
	Эта функция запускается только после запуска самого Telegram-бота.
	"""

	logger.info("Привет, мир! Бот загружен.")

if __name__ == "__main__":
	# Запускаем самого Telegram-бота.

	loop = asyncio.new_event_loop()
	asyncio.set_event_loop(loop)

	aiogram.utils.executor.start_polling(
		dispatcher=DP,
		on_startup=onBotStart,
		skip_updates=True,
		loop=loop
	)
