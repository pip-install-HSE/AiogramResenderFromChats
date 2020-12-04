from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

got_it_markup = ReplyKeyboardMarkup()
got_it_markup.add(KeyboardButton('Спасибо, понятно'))

menu_markup = ReplyKeyboardMarkup()
menu_markup.add(KeyboardButton('📡 Поисковые слова'))
menu_markup.add(KeyboardButton('⛔️ Стоп-слова'))
menu_markup.add(KeyboardButton('💻 Мини-курс'))
menu_markup.add(KeyboardButton('☎️ Отдел заботы'))

back_markup = ReplyKeyboardMarkup()
back_markup.add(KeyboardButton('<< В меню'))

'''
📡 Поисковые слова
⛔️ Стоп-слова
💻 Мини-курс
☎️ Отдел заботы
'''