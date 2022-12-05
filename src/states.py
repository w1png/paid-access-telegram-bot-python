from aiogram.dispatcher.filters.state import State, StatesGroup

class addPromocode(StatesGroup):
    name = State()
    value = State()
    is_percent = State()
    max_uses = State()
    first_order_only = State()
    expires = State()

