from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from ui.text import PHRASES

router = Router()

@router.message(Command('start')) 
async def cmd_start(message: types.Message, state: FSMContext): 
    await state.clear()
    await message.answer(PHRASES['start'])


@router.message(Command('info')) 
async def cmd_info(message: types.Message): 
    await message.answer(PHRASES['info'])
