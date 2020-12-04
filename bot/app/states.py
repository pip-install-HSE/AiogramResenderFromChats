from aiogram.dispatcher.filters.state import StatesGroup, State


class Variants(StatesGroup):
	start_info = State()
	menu = State()
	search_update = State()
	stopwords_update = State()