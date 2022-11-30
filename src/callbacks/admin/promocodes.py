import models
from aiogram import types
import markups
from constants import language


async def execute(user: models.users.User, query: types.CallbackQuery, data: dict) -> None:
    return await query.message.edit_text(
        text=language.promocodes,
        reply_markup=markups.create_markup([
            (language.admin_add_promocode, "admin_addPromocode{}"),
            (language.admin_remove_promocode, "admin_removePromocode{}"),
            (language.admin_edit_promocode, "admin_editPromocode{}"),
            (language.back, 'admin_adminPanel{}')
        ])
    )

