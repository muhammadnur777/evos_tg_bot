from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db


def make_categories_kb(cart_exists = False):
    categories = db.get_all_category()
    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = []

    if cart_exists:
        menu.add(
            KeyboardButton(text='📥Savat')
        )
    for category in categories:
        buttons.append(
            KeyboardButton(text=category[-1])
        )

    menu.add(*buttons)
    menu.add(
        KeyboardButton(text="⬅️ Ortga"),
        KeyboardButton(text='Savatcha 📥')
    )
    return menu
