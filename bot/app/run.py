from aiogram import executor, Dispatcher

from core import dp, db, bot, logger
import dispatcher


async def startup(dispatcher: Dispatcher):
    return True


async def shutdown(dispatcher: Dispatcher):
    # Close Mongo Sorage
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()
    # Close Database
    await db.close()
    return True


if __name__ == "__main__":
    executor.start_polling(dp,
                         skip_updates=True,
                         timeout=5,
                         on_startup=startup,
                         on_shutdown=shutdown)
