import models

from aiogram import types
import markups
from constants import language


async def execute(user: models.users.User, query: types.CallbackQuery | types.Message, data: dict):
    markup = [
        (item.name, f"user_item{'i': item.id}")
        for item in models.items.get_items()
    ]
    markup.append((language.close, "user_close{}"))
    text = language.items

    if isinstance(query, types.CallbackQuery):
        return await query.message.edit_text(
            text=text,
            reply_markup=markups.create_markup(markup)
        )
    return await query.answer(
        text=text,
        reply_markup=markups.create_markup(markup)
    )

