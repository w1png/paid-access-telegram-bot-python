import models
from aiogram import types
import markups
from constants import language


async def execute(user: models.users.User, query: types.CallbackQuery, data: dict) -> None:
    return await query.message.edit_text(
        text=,
        reply_markup=
    )

