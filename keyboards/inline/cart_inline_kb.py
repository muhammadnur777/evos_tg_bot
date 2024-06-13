from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import db
import random


def cart_inline():
    menu = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(text='⬅️ Ortga', callback_data='cart_inline_back'),
                InlineKeyboardButton(text='🚖 Buyurtma Berish', callback_data='ordering')
            ],
            [
                InlineKeyboardButton(text='🗑 Savatni tozalash', callback_data='clear_cart')
            ]
        ])
    return menu


def prepare_to_make_products_inline(data: list|tuple):
    tugmalar = []
    for user_id, product_id, quantity, product_type in data:
        product_name = db.get_product_name(product_id)[0]

        tugmalar.append(
            InlineKeyboardButton(
                text=f"❌ {product_name}",
                callback_data=f'cancel.{product_id}.{product_name}'
            )
        )
    return tugmalar

def cart_inline_products(tg_id):
    data = db.get_order(tg_id) # bazadan user_id, product_id, quantity
    
    # tugmalarni yasash qismi
    menu = cart_inline()
    menu.row_width = 1
    inline_products = prepare_to_make_products_inline(data)
    menu.add(*inline_products)

    # savat matnini yasash qismi
    text = make_products_text(data)

    return menu, text


def make_products_text(data: list):
    base_text = ''''''
    product_text = '''{} ✖️ {}\n'''
    jami = 0
    for user_id, product_id, quantity, product_type in data:
        product_name = db.get_product_name(product_id)
        base_text += product_text.format(quantity, product_name[0])
        price = db.get_product_price(product_type)
        jami += price[0]

    base_text += f'jami: {jami}'
    
    return base_text









def cart_inline_products2(tg_id):
    data = db.get_order(tg_id) 
    
    
    text = make_products_text2(tg_id, data)
    
    return text


def make_products_text2(tg_id: int, data: list):
    locations = db.get_user_locations(tg_id)  
    location_text = ', '.join([location[0] for location in locations])
    
    base_text = f'Sizning buyurtmangiz\nManzil: {location_text}\n'
    product_text = '{} ✖️ {}\n'
    jami = 0

    for user_id, product_id, quantity, product_type in data:
        product_name = db.get_product_name(product_id)
        base_text += product_text.format(quantity, product_name[0])
        price = db.get_product_price(product_type)
        jami += price[0]

    base_text += f'jami: {jami} \nYetkazib berish: 12 000 som'
    
    return base_text








def cart_inline_products3(tg_id):
    data = db.get_order(tg_id) 
    
    
    text = make_products_text2(tg_id, data)
    
    return text

def generate_random_8_digit_number():
    return random.randint(10000000, 99999999)


def make_products_text3(tg_id: int, data: list):
    locations = db.get_user_locations(tg_id)  
    location_text = ', '.join([location[0] for location in locations])
    random_number = generate_random_8_digit_number() 



    base_text = f'Buyurtma raqami:{random_number}\nHolat: Yangi\nManzil: {location_text}\n'
    product_text = '{} ✖️ {}\n'
    jami = 0

    for user_id, product_id, quantity, product_type in data:
        product_name = db.get_product_name(product_id)
        base_text += product_text.format(quantity, product_name[0])
        price = db.get_product_price(product_type)
        jami += price[0]

    base_text += f'jami: {jami} \nYetkazib berish: 12 000 som\nBuyurtmangiz qabul qilindi.\nYetkazib berish vaqti - 30 daqiqa'
    
    return base_text
