import logging
import os
from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)
API_TOKEN_BOT = os.getenv('API_TOKEN')
bot = Bot(token=API_TOKEN_BOT)

# executor.start_polling(dp, skip_updates=True)
