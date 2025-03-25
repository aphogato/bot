from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from datetime import datetime, timedelta

from handlers.parser import date
from handlers.cities import CITY_NAMES

def city_keyboard():
    builder = InlineKeyboardBuilder()
    for city in CITY_NAMES:
        builder.add(InlineKeyboardButton(text=city, callback_data=city))
    builder.adjust(2)

    return builder.as_markup()

def date_keyboard():
    builder = InlineKeyboardBuilder()
    today = datetime.now()
    for i in range(0, 7):
        future_date = today + timedelta(days=i)
        formatted_date = future_date.strftime("%Y-%m-%d")
        builder.add(InlineKeyboardButton(text=date(formatted_date), callback_data=str(i)))
        builder.adjust(1)

    return builder.as_markup()