from main import bot, dp
from aiogram import types
from aiogram.types import WebAppInfo
 


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    web_app = WebAppInfo(url='https://foodbotsite.netlify.app/')
 
    
    button = types.InlineKeyboardButton(text='BotHub', web_app=web_app)
    markup = types.InlineKeyboardMarkup()
    markup.add(button)

    await message.reply("🇷🇺 Давайте начнем 🍔 Пожалуйста, нажмите на кнопку ниже, чтобы открыть список! \n\n🇺🇿 Keling, boshlaymiz 🍔 Roʻyxatni ochish uchun pastdagi tugmani bosing!",
                        reply_markup=markup)
    
    
