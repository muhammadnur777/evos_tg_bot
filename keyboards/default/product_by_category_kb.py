from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db


def make_products_kb(category_name: str, cart_exists = False):
    mahsulotlar = db.get_products_by_category(category_name)

    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    tugmalar = []
    if cart_exists:
        menu.add(
            KeyboardButton(text='📥Savat')
        )

    for mahsulot in mahsulotlar:
        tugmalar.append(
            KeyboardButton(text=mahsulot[0])
        )

    menu.add(*tugmalar)
    menu.add(
        KeyboardButton(text="⬅️ Ortga"),
        KeyboardButton(text='Savatcha 📥')
    )
    return menu

