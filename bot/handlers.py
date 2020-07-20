from main import bot, dp
from aiogram.types import Message
from config import admin_id
from index import b1_calcpay1, b1_register1,b1
import keyBoards as kb
from aiogram import Bot, Dispatcher, executor, types
from string import Template

async def send_to_admin(dp):
     await bot.send_message(chat_id=admin_id, text='Бот запущен')



@dp.message_handler(commands=['start'])
async def Calcpay(message: types.Message):
          await bot.send_message(message.from_user.id,
                              text=b1, reply_markup=kb.greet_kb)
@dp.message_handler(commands=[f'/Калькулятор зарплаты'])
async def Calcpay(message: types.Message):
          await bot.send_message(message.from_user.id,
                              text=b1_calcpay1, reply_markup=kb.greet_kb)


