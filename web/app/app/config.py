from os import getenv

# Database configurations
PG_HOST = getenv("PG_HOST", '0.0.0.0')
PG_PORT = getenv("PG_PORT", 5400)

PG_USER_NAME = getenv("POSTGRES_USER", 'myuser')
PG_DATABASE_NAME = getenv("POSTGRES_DB", 'mydb')
PG_USER_PASSWORD = getenv("POSTGRES_PASSWORD", 'scryPass01sec')
