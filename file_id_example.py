import asyncio
import logging
from aiogram import Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from config import TOKEN
from aiogram import Bot

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"<b>Assalomu Aleykum, Xurmatli {message.from_user.mention_html()}</b>")


@dp.message()
async def handle_document(message: types.Message, bot: Bot):
    photo = message.photo[-1]
    file_id = photo.file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path
    file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    await message.answer("File id:", file_url)
    await message.answer_photo(file_id)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
