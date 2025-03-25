from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters.command import Command 
from aiogram.types import Message, CallbackQuery

from ui.keyboards import city_keyboard, date_keyboard

from ui.text import PHRASES

from handlers.parser import weather, osadki, temperature, check_city

router = Router()

class Weather(StatesGroup):
    selecting_city = State()
    selecting_date = State()

@router.message(Command('cities'))
async def cmd_cities(message: Message, state: FSMContext):
    await message.answer(
        text=PHRASES['city'],
        reply_markup=city_keyboard()
    )
    await state.set_state(Weather.selecting_city)


@router.callback_query(Weather.selecting_city)
async def city_selected_via_button(callback: CallbackQuery, state: FSMContext):
    await city_selected(callback.data, callback.message, state)
    await callback.answer()


@router.message(Weather.selecting_city)
async def city_selected_via_text(message: Message, state: FSMContext):
    await city_selected(message.text, message, state)


async def city_selected(city: str, message: Message, state: FSMContext):
    if check_city(city):
        await state.update_data(selected_city=city)
        await message.answer(
            text=PHRASES['date'].replace('#', city), 
            reply_markup=date_keyboard()
        )
        await state.set_state(Weather.selecting_date)
    else:
        await message.answer(PHRASES['city_error'])


@router.callback_query(Weather.selecting_date, F.data != None)
async def sending_weather(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    city = data['selected_city']
    start_index = int(callback.data)
    await callback.message.answer("ночь: " + weather(city)[start_index] + ", " + temperature(city)[start_index] + ", осадки: " + osadki(city)[start_index])
    await callback.message.answer("утро: " + weather(city)[start_index + 1] + ", " + temperature(city)[start_index+1] + ", осадки: " + osadki(city)[start_index+1])
    await callback.message.answer("день: " + weather(city)[start_index + 2] + ", " + temperature(city)[start_index+2] + ", осадки: " + osadki(city)[start_index+2])
    await callback.message.answer("вечер: " + weather(city)[start_index + 3] + ", " + temperature(city)[start_index+3] + ", осадки: " + osadki(city)[start_index+3])