from aiogram import Router, F, types
from pathlib import Path
from aiogram.types import InputMediaPhoto
from aiogram.filters import CommandStart
from keyboard import get_callback_btns
from randomizer import create_num


user_router = Router()

@user_router.message(CommandStart)
async def start(message: types.Message):
    await message.answer("Hello, this is bot for english practice. Tap the button👇", reply_markup=get_callback_btns(
        btns={
            "Give me an exercise": f'random'
        }
    ))





@user_router.callback_query(F.data == 'random')
async def card(callback: types.CallbackQuery):
    try:
        # 1. Генерируем случайное число
        number = await create_num(low_num=1, high_num=20)

        # 2. Ищем все файлы начинающиеся с "{number}-"
        photo_dir = Path('C:/Users/admin/PycharmProjects/Lenabot/.venv/photos')
        photo_files = sorted(photo_dir.glob(f'{number}-*.jpg'))

        if not photo_files:
            raise FileNotFoundError(f"Нет фото для номера {number}")

        # 3. Создаем медиагруппу
        media_group = [
            InputMediaPhoto(media=types.FSInputFile(path))
            for path in photo_files
        ]

        await callback.message.answer_media_group(media=media_group)

        await callback.message.answer(
            text="Choose an action:",
            reply_markup=get_callback_btns(btns={"Next": "random"})
        )

    except Exception as e:
        await callback.message.answer(f"⚠️ Ошибка: {str(e)}")
    finally:
        await callback.answer()
