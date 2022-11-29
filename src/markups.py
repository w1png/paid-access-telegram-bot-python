from aiogram import types
import constants

def create_markup(buttons: list[tuple[str, str]], inline: bool=True) -> types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup:
    markup = types.InlineKeyboardMarkup() if inline else types.ReplyKeyboardMarkup(resize_keyboard=True)
    for button in buttons:
        markup.add(types.InlineKeyboardButton(button[0], callback_data=button[1]) if inline else types.KeyboardButton(button[0]))
    return markup


main_markup = create_markup([
    (constants.language.items, "user_items{}"),
], inline=False)

