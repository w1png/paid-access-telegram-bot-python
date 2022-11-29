import models
from aiogram import types
import markups
from constants import language


async def execute(user: models.users.User, query: types.CallbackQuery, data: dict) -> None:
    await query.message.delete()

