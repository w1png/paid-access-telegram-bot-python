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
import markups


# First startup
if not os.path.exists("database.db"):
    utils.database.execute("PRAGMA foreign_keys = ON")
    for model in [models.users, models.items, models.promocodes, models.payments]:
        print(f"Creating table {model.__name__}")
        utils.database.execute(model.get_database_table())

    models.users.create(constants.config["main_admin_id"], is_admin=True,)

if not os.path.exists("config.json"):
    raise FileNotFoundError("config.json не найден. Запустите setup.py для его создания.")

storage = MemoryStorage()
bot = Bot(token=constants.TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user = models.users.User(message.from_user.id)

    await message.answer(
        utils.config["info"]["greeting"],
        reply_markup=markups.main_markup
    )


@dp.message_handler()
async def main_menu(message: types.Message):
    user = models.users.User(message.from_user.id)

    destination = ""
    role = "user"
    if message.text == constants.language.items:
        destination = "items"
    else:
        return await message.answer(constants.language.unknown_command)

    return await importlib.import_module(f"callbacks.{role}.{destination}").execute(user, message, None)


def parse_callback(callback: str):
    role = callback.split("_")[0]
    call = callback[callback.find("_") + 1:callback.find("{")]
    data = json.loads(callback[callback.find("{"):])
    return role, call, data


@dp.callback_query_handler()
async def callback_handler(query: types.CallbackQuery):
    role, call, data = parse_callback(query.data)
    user = models.users.User(query.from_user.id)

    if role == "admin" and not user.is_admin(user):
        return await utils.send_no_permission(query.answer)

    return await importlib.import_module(f"callbacks.{role}.{call}").execute(user, query, data)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

