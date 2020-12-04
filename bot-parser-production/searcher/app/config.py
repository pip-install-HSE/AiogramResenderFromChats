from os import getenv

shared = getenv("SHARED_FOLDER", 'shared/')

"""
TELEGRAM
"""

api_id = 1910100
api_hash = '34d7b194d662b5c343fc43268f8dc78d'
api_sess_name = 'anon' # anon.session

target_chat_id = -1001391033195 # found messages will be posted here
link_template = "https://t.me/c/{{chat_id}}/{{message_id}}"

ignore_chats = [-1001391033195]

joiner = ", "
pattern = "[^a-zа-яёїієґ0-9_-]{{phrase}}[^a-zа-яёїієґ0-9_-]"

keywords_file = shared + 'keywords.txt'
stopwords_file = shared + 'stopwords.txt'

PG_HOST = getenv("PG_HOST", 'localhost')
PG_PORT = getenv("PG_PORT", '5400')

PG_USER_NAME = getenv("POSTGRES_USER", 'myuser')
PG_DATABASE_NAME = getenv("POSTGRES_DB", 'mydb')
PG_USER_PASSWORD = getenv("POSTGRES_PASSWORD", 'scryPass01sec')