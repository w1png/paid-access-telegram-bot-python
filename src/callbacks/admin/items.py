import models
from aiogram import types
import markups
from constants import language


async def execute(user: models.users.User, query: types.CallbackQuery, data: dict) -> None:
    return await query.message.edit_text(
        text=language.items,
        reply_markup=markups.create_markup([
            (language.admin_add_item, "admin_addItem{}"),
            (language.admin_remove_item, "admin_removeItem{}"),
            (language.admin_edit_item, "admin_editItem{}"),
            (language.admin_add_item_to_user, "admin_addItemToUser{}"),
            (language.back, 'admin_back{"rd":"adminPanel"}'),
        ])
    )

