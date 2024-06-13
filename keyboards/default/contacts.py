from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db


menu_for_contacts = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="📞 Mening raqamim", request_contact=True)
            
        ],
        [
            KeyboardButton(text='⬅️ Ortga')
        ]
   
    ]
)

payments = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Naqd pul")
         
        ],
        [KeyboardButton(text='Click')],
        [KeyboardButton(text='Payme')],
        [KeyboardButton(text='⬅️ Ortga')]

    ]
)


confirmation = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text='✅ Tasdiqlash')],
        [KeyboardButton(text='❌ Bekor qilish')]
    ]
)