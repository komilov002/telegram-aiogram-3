from aiogram import Router, types
from googletrans import Translator


translate = Translator()


router = Router()


@router.message()
async def start_user(message: types.Message):
    xabar = message.text
    a = translate.translate(text=xabar, dest='ru')
    await message.answer(text=a)
