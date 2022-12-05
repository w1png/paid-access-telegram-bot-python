import models
from aiogram import types
import markups
from constants import language
import states

async def execute(user: models.users.User, query: types.CallbackQuery, data: dict) -> None:
    await states.addPromocode.name.set()

    return await query.message.edit_text(
        text=language.add_promocode_name,
        reply_markup=markups.create_markup([(language.cancel, 'admin_cancel{"rd": "promocodes}')]),
    )

