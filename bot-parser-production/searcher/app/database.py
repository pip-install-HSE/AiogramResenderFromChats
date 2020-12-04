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


  async def check_sign(self, s1, s2):
    pool = await self.get_pool()
    async with pool.acquire() as conn:
      q = "SELECT 1 FROM administration_chatmessage WHERE first_digest = $1 AND second_digest = $2"
      row = await conn.fetchrow(q, s1, s2)
    return dict(row) if row else None


  async def add_sign(self, s1, s2, name, username):
    res = None
    pool = await self.get_pool()
    async with pool.acquire() as conn:
      q = """INSERT INTO administration_chatmessage
        (first_digest, second_digest, sender_name, sender_username, created_at)
        VALUES ($1, $2, $3, $4, NOW())
      """
      res = await conn.execute(q, s1, s2, name, username)
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
