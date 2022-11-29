import models
from aiogram import types
import markups
from constants import language


async def execute(user: models.users.User, query: types.CallbackQuery, data: dict) -> None:
    markup = markups.create_markup([
        (language.items, "admin_items{}"),
        (language.close, "user_close{}"),
    ])
    text = language.admin_panel

    if isinstance(query, types.CallbackQuery):
        return await query.message.edit_text(
            text=text,
            reply_markup=markup
        )
    return await query.answer(
        text=text,
        reply_markup=markup
    )

