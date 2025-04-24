import asyncio
from aiogram import Bot,Dispatcher
from handlers import user_router



bot = Bot(token='7746448175:AAG1Ph1g8zmQQ1vLkXjkIuZVM0NtXfHQu3A')

dp = Dispatcher()

async def main():
    dp.include_router(user_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())