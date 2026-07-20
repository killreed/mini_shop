from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards import main_menu

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Добро пожаловать в Mini Shop!",
        reply_markup=main_menu,
    )