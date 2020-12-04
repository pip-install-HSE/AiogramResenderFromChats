from aiogram import types
from aiogram.utils.exceptions import MessageCantBeDeleted, BotBlocked

from core import dp, db, logger
from states import Variants
import handlers


'''
📡 Поисковые слова
⛔️ Стоп-слова
💻 Мини-курс
☎️ Отдел заботы
'''


dp.register_message_handler(handlers.start, chat_type=['private'], commands='start', state='*')
dp.register_message_handler(handlers.start_info, chat_type=['private'], text='Спасибо, понятно', state=Variants.start_info)

dp.register_message_handler(handlers.back, chat_type=['private'], text='<< В меню', state='*')

dp.register_message_handler(handlers.links, lambda msg: 'reply_to_message' in msg and msg.text == '/link', chat_type=['private'], state='*')

dp.register_message_handler(handlers.search_words, chat_type=['private'], text='📡 Поисковые слова', state=Variants.menu)
dp.register_message_handler(handlers.stop_words, chat_type=['private'], text='⛔️ Стоп-слова', state=Variants.menu)
dp.register_message_handler(handlers.menu_course, chat_type=['private'], text='💻 Мини-курс', state=Variants.menu)
dp.register_message_handler(handlers.menu_support, chat_type=['private'], text='☎️ Отдел заботы', state=Variants.menu)

dp.register_message_handler(handlers.search_words_update, chat_type=['private'], state=Variants.search_update)
dp.register_message_handler(handlers.stop_words_update, chat_type=['private'], state=Variants.stopwords_update)

dp.register_message_handler(handlers.new_message, chat_type=['supergroup'], chat_id=-1001391033195, user_id=1259979988, state='*')
dp.register_message_handler(handlers.new_message_caption, content_types=['photo', 'video'], chat_type=['supergroup'], chat_id=-1001391033195, user_id=1259979988, state='*')

dp.register_errors_handler(handlers.handle_MessageCantBeDeleted, exception=MessageCantBeDeleted)
dp.register_errors_handler(handlers.handle_BotBlocked, exception=BotBlocked)