# coding: utf-8

import importlib
import os
from typing import Tuple

import aiogram
import dotenv
from aiogram import Bot, Dispatcher
from loguru import logger

# Загружаем все переменные из .env-файла:
dotenv.load_dotenv()

# Инициализируем бота:
BOT = Bot(
	os.environ["TOKEN"],
	parse_mode=aiogram.types.ParseMode.HTML
)

DP = Dispatcher(BOT)

def getTelegramBot() -> Tuple[Bot, Dispatcher]:
	"""
	Выдаёт Tuple с `aiogram.Bot`, `aiogram.Dispatcher`.
	"""

	loadBotHandlers()

	return (BOT, DP)
	
def loadBotHandlers():
	"""
	Загружает все Handler'ы для Telegram-бота, что находятся в папке `BotHandlers`. Под-папки будут проигнорированы.
	"""

	files = [
		f"BotHandlers.{os.path.splitext(i)[0]}" # Выдаёт: BotHandlers.filename

		for i in os.listdir("BotHandlers") 

		if os.path.isfile(						# Только *файлы* могут быть загружены.
			os.path.join(
				os.getcwd(), "BotHandlers", i
			)
		)
	]

	logger.debug(f"Было обнаружено {len(files)} файлов в папке \"BotHandlers\".")

	for file in files:
		logger.debug(f"Импортирую модуль {file}...")
		handler_module = importlib.import_module(file)

		if "initThisHandler" not in handler_module.__dict__:
			logger.warning("В модуле \"{file}\" нет инициализирующей функции \"initThisHandler\", пропускаю этот модуль...")

			continue

		# Вызываю функцию initThisHandler, что бы у Handler'а 
		# были установлены глобальные переменные BOT и DP.

		handler_module.initThisHandler(BOT, DP)
