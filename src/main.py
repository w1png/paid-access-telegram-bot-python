import asyncio
import os
import importlib
import logging
import sys
import json

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

import constants
import models
import utils


# First startup
if not os.path.exists("database.db"):
    utils.database.execute("PRAGMA foreign_keys = ON")
    for model in [models.users, models.items, models.promocodes, models.payments]:
        print(f"Creating table {model.get_database_table()}")
        utils.database.execute(model.get_database_table())
if not os.path.exists("config.json"):
    raise FileNotFoundError("config.json не найден. Запустите setup.py для его создания.")

storage = MemoryStorage()
bot = Bot(token=constants.TOKEN)
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        utils.config["info"]["greeting"]
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

