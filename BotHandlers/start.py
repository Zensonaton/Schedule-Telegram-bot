# coding: utf-8

from aiogram import Bot, Dispatcher
from aiogram.types import Message as MessageType
from loguru import logger

BOT: Bot = None 		# type: ignore
DP: Dispatcher = None 	# type: ignore

def initThisHandler(bot: Bot, dp: Dispatcher):
	"""
	Инициализирует этот Handler.
	"""

	global BOT, DP

	BOT = bot
	DP = dp

	DP.message_handler(commands=["start", "help"])(start_command)

async def start_command(msg: MessageType):
	await msg.answer("Привет! :)")
