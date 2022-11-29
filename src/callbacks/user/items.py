import models

from aiogram import types
import markups
from constants import language


async def execute(user: models.users.User, query: types.CallbackQuery | types.Message, data: dict):
    message = query
    if not isinstance(query, types.Message):
        message = query.message

    markup = [
            (item.name, f"user_item{'i': item.id}")
        for item in models.items.get_items()
    ]
    markup.append((language.close, "user_close{}"))

    return await message.answer(
        text=language.items,
        reply_markup=markups.create_markup(markup)
    )

