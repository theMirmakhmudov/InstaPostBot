import asyncio
import logging
from aiogram import Dispatcher, F, types
from aiogram.client import bot
from aiogram.enums import ParseMode, MessageEntityType
from aiogram.filters import Command
from config import TOKEN
from aiogram import Bot
import numpy as np

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Assalomu Aleykum, Xurmatli {message.from_user.mention_html()}")


@dp.message(F.photo)
async def check_photo_qr_code(message: types.Message, bot: Bot):
    import cv2
    from pyzbar.pyzbar import decode
    file_id = message.photo[-1].file_id

    # Get file path
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path

    # Download the photo
    file = await bot.download_file(file_path)

    # Convert downloaded file to numpy array
    nparr = np.frombuffer(file.read(), np.uint8)

    # Decode the image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Find and decode QR codes
    for barcode in decode(img):
        mydata = barcode.data.decode("utf-8")
        print(mydata)

        await message.answer(f"Data: {mydata}")

    # cv2.imshow("Image", img)
    # cv2.waitKey(1)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
