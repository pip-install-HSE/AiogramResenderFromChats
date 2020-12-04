from os import getenv

MONGO_HOST = getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(getenv("MONGO_PORT", 27000))

PG_HOST = getenv("PG_HOST", 'localhost')
PG_PORT = getenv("PG_PORT", '5400')

PG_USER_NAME = getenv("POSTGRES_USER", 'myuser')
PG_DATABASE_NAME = getenv("POSTGRES_DB", 'mydb')
PG_USER_PASSWORD = getenv("POSTGRES_PASSWORD", 'SOMEPASSWORD')


TOKEN = getenv("BOT_TOKEN", "SOMETOKEN")

SHARED_FOLDER = "shared/"
#SHARED_FOLDER = "shared/"
SHARED_FILES = SHARED_FOLDER + 'files/'

PATTERN = "[^a-zа-яёїієґ0-9_-]{{phrase}}[^a-zа-яёїієґ0-9_-]"
