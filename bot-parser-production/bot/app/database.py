import asyncpg
import asyncio

import config


class Database:

    def __init__(self):
        self.host = config.PG_HOST
        self.port = config.PG_PORT
        self.database = config.PG_DATABASE_NAME
        self.user = config.PG_USER_NAME
        self.password = config.PG_USER_PASSWORD

        self.pool = None


    async def get_username_by_sign(self, s1, s2):
        pool = await self.get_pool()
        async with pool.acquire() as conn:
            q = "SELECT sender_username FROM administration_chatmessage WHERE first_digest = $1 AND second_digest = $2"
            row = await conn.fetchrow(q, s1, s2)
        return dict(row) if row else None


    async def get_all_words(self):
        pool = await self.get_pool()
        async with pool.acquire() as conn:
            q = "SELECT * FROM administration_word"
            rows = await conn.fetch(q)
        return rows

    async def get_words(self, uid):
        pool = await self.get_pool()
        async with pool.acquire() as conn:
            q = "SELECT * FROM administration_word WHERE user_id = $1"
            row = await conn.fetchrow(q, uid)
        return dict(row) if row else None

    async def search_words_update(self, uid, search_words):
        res = None
        try:
            pool = await self.get_pool()
            async with pool.acquire() as conn:
                q = """INSERT INTO administration_word
                    (user_id, search_words)
                    VALUES ($1, $2)
                    ON CONFLICT (user_id) DO UPDATE
                    SET search_words = EXCLUDED.search_words"""
                res = await conn.execute(q, uid, search_words)
        except Exception as e:
            print(str(e))
        return res

    async def stop_words_update(self, uid, stop_words):
        res = None
        try:
            pool = await self.get_pool()
            async with pool.acquire() as conn:
                q = """INSERT INTO administration_word
                    (user_id, stop_words)
                    VALUES ($1, $2)
                    ON CONFLICT (user_id) DO UPDATE
                    SET stop_words = EXCLUDED.stop_words"""
                res = await conn.execute(q, uid, stop_words)
        except Exception as e:
            print(str(e))
        return res

    async def get_msg(self, name):
        pool = await self.get_pool()
        async with pool.acquire() as conn:
            q = "SELECT * FROM administration_message WHERE name = $1"
            row = await conn.fetchrow(q, name)
        return dict(row) if row else None

    async def get_user_by_id(self, uid):
        pool = await self.get_pool()
        async with pool.acquire() as conn:
            q = "SELECT * FROM administration_user WHERE id = $1"
            row = await conn.fetchrow(q, uid)
        return dict(row) if row else None

    async def save_user(self, uid, name, last_name, username):
        res = None
        try:
            pool = await self.get_pool()
            async with pool.acquire() as conn:
                q = """INSERT INTO administration_user
                    (id, name, lastname, username, created_at, updated_at)
                    VALUES ($1, $2, $3, $4, NOW(), NOW())
                    ON CONFLICT (id) DO UPDATE
                    SET name = EXCLUDED.name,
                    lastname = EXCLUDED.lastname,
                    username = EXCLUDED.username,
                    updated_at = NOW()"""
                res = await conn.execute(q, uid, name, last_name, username)
        except Exception as e:
            print(str(e))
        return res

    async def get_file_id(self, filename):
        pool = await self.get_pool()
        async with pool.acquire() as conn:
            q = "SELECT * FROM administration_file WHERE file_name = $1"
            row = await conn.fetchrow(q, filename)
        return dict(row) if row else None

    async def add_file(self, file_name, file_id):
        res = None

        try:
            pool = await self.get_pool()
            async with pool.acquire() as conn:
                q = """INSERT INTO administration_file (file_name, file_id)
                    VALUES ($1, $2)
                    ON CONFLICT (file_name)
                    DO UPDATE
                    SET file_name = EXCLUDED.file_name, file_id = EXCLUDED.file_id"""
                res = await conn.execute(q, file_name, file_id)
        except Exception as e:
            print(str(e))
        return res

    async def set_pool(self):
        self.pool = await asyncpg.create_pool(host=self.host,
                                              port=self.port,
                                              database=self.database,
                                              user=self.user,
                                              password=self.password)
        return self.pool

    async def get_pool(self):
        if self.pool:
            return self.pool
        return await self.set_pool()

    async def close(self):
        if self.pool:
            await self.pool.close()
        self.pool = None
