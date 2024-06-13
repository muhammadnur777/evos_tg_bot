from aiogram.dispatcher.filters.state import StatesGroup, State


class UserState(StatesGroup):
    location = State()
    sub_location = State()
    product_selection = State()
    mahsulot_tanlash = State()
    ordering = State()
    payment = State()  
    order_confirmation = State() 
    confirmation = State()
    confirmation2 = State()