import asyncio
import logging
from aiogram import Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from config import TOKEN
from aiogram import Bot
from aiogram.types import BufferedInputFile

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"<b>Assalomu Aleykum, Xurmatli {message.from_user.mention_html()}</b>")
    print(message.from_user.id)


@dp.message()
async def generator_qr_code(message: types.Message):
    import qrcode

    data = message.text
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr-data.png")
    file_ids = []

    with open("qr-data.png", "rb") as photo:
        result = await message.answer_photo(
            BufferedInputFile(
                photo.read(),
                filename="qr-data.png"
            ))

        file_ids.append(result.photo[-1].file_id)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
