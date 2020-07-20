from aiogram.types import ReplyKeyboardMarkup, \
                            KeyboardButton
btnCalcpay = KeyboardButton("/Калькулятор зарплаты")
greet_kb =ReplyKeyboardMarkup(resize_keyboard=True).add(btnCalcpay)