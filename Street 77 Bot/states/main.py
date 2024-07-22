from aiogram.dispatcher.filters.state import State, StatesGroup

class Example(StatesGroup):
    menu = State()
    delivery_type = State()
    yetkazish = State()
    olib_ketish = State()