from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode
from utils.db.postgres import Database
from data.config import BOT_TOKEN
from aiogram.client.bot import DefaultBotProperties

db = Database()
# bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)
