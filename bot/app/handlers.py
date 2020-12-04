from hashlib import md5
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
import asyncio

from states import Variants
from core import db, bot, logger
from functions import send_video, check_matches, update_global_keywords, clear_message
from markups import got_it_markup, menu_markup, back_markup


async def start(message: types.Message, state: FSMContext):

    uid = message.from_user.id
    user = await db.get_user_by_id(uid)

    if not user:

        await db.save_user(
            message.from_user.id,
            message.from_user.first_name,
            message.from_user.last_name,
            message.from_user.username
        )

        await bot.send_chat_action(uid, 'typing')
        msg_welcome = (await db.get_msg('start-video'))['message']
        msg_welcome = msg_welcome.replace('{{username}}', message.from_user.first_name)
        await message.answer(msg_welcome)

        await bot.send_chat_action(uid, 'typing')
        await asyncio.sleep(1)
        msg_next = (await db.get_msg('start-welcome'))['message']
        await message.answer(msg_next)

        await bot.send_chat_action(uid, 'upload_photo')
        #await asyncio.sleep(1)
        #await send_video(uid, 'startvideo.mp4')
        with open('shared/files/intro.jpg', 'rb') as photo:
            await message.answer_photo(photo, caption=None)

        await bot.send_chat_action(uid, 'typing')
        await asyncio.sleep(1)
        msg_next = (await db.get_msg('start-button'))['message']
        await message.answer(msg_next, reply_markup=got_it_markup)

        await bot.send_chat_action(uid, 'typing')
        msg_next = (await db.get_msg('start-button-click'))['message']
        await message.answer(msg_next)

        await Variants.start_info.set()

    else:

        await bot.send_chat_action(uid, 'typing')
        msg = (await db.get_msg('menu'))['message']
        await message.answer(msg, reply_markup=menu_markup)

        await Variants.menu.set()

    return True


async def start_info(message: types.Message, state: FSMContext):

    uid = message.from_user.id
    user = await db.get_user_by_id(uid)

    await bot.send_chat_action(uid, 'typing')
    await asyncio.sleep(1)
    msg_next = (await db.get_msg('start-menu-first'))['message']
    await message.answer(msg_next, reply_markup=ReplyKeyboardRemove())

    await bot.send_chat_action(uid, 'typing')
    await asyncio.sleep(1)
    msg = (await db.get_msg('menu'))['message']
    await message.answer(msg, reply_markup=menu_markup)

    await Variants.menu.set()

    return True


async def back(message: types.Message, state: FSMContext):
    uid = message.from_user.id
    user = await db.get_user_by_id(uid)

    await bot.send_chat_action(uid, 'typing')
    msg = (await db.get_msg('menu'))['message']
    await message.answer(msg, reply_markup=menu_markup)

    await Variants.menu.set()

    return True


async def menu_course(message: types.Message, state: FSMContext):

    uid = message.from_user.id
    user = await db.get_user_by_id(uid)

    await bot.send_chat_action(uid, 'typing')
    msg = (await db.get_msg('course'))['message']
    await message.answer(msg)

    return True


async def menu_support(message: types.Message, state: FSMContext):

    uid = message.from_user.id
    user = await db.get_user_by_id(uid)

    await bot.send_chat_action(uid, 'typing')
    msg = (await db.get_msg('support'))['message']
    await message.answer(msg)

    return True


async def search_words(message: types.Message, state: FSMContext):
    uid = message.from_user.id
    user = await db.get_user_by_id(uid)
    words = await db.get_words(uid)

    if words and words['search_words']:

        await bot.send_chat_action(uid, 'typing')
        msg = (await db.get_msg('search-set'))['message']
        await message.answer(msg)

        await bot.send_chat_action(uid, 'typing')
        await message.answer('<i>' + words['search_words'] + '</i>')

        msg = (await db.get_msg('search-update'))['message']
        await message.answer(msg, reply_markup=back_markup)

    else:

        await bot.send_chat_action(uid, 'typing')
        msg = (await db.get_msg('search-unset'))['message']
        await message.answer(msg)

        msg = (await db.get_msg('search-update'))['message']
        await message.answer(msg, reply_markup=back_markup)

    await Variants.search_update.set()

    return True


async def stop_words(message: types.Message, state: FSMContext):
    uid = message.from_user.id
    user = await db.get_user_by_id(uid)
    words = await db.get_words(uid)

    if words and words['stop_words']:

        await bot.send_chat_action(uid, 'typing')
        msg = (await db.get_msg('stop-set'))['message']
        await message.answer(msg)

        await bot.send_chat_action(uid, 'typing')
        await message.answer('<i>' + words['stop_words'] + '</i>')

        msg = (await db.get_msg('stop-update'))['message']
        await message.answer(msg, reply_markup=back_markup)

    else:

        await bot.send_chat_action(uid, 'typing')
        msg = (await db.get_msg('stop-unset'))['message']
        await message.answer(msg)

        msg = (await db.get_msg('stop-update'))['message']
        await message.answer(msg, reply_markup=back_markup)

    await Variants.stopwords_update.set()

    return True


async def search_words_update(message: types.Message, state: FSMContext):

    words = message.text.strip().lower()
    words = words[:-1] if words and words[-1] == ',' else words
    words = ', '.join(sorted(list(set(list(map(lambda word: word.strip(), words.split(',')))))))
    await db.search_words_update(message.from_user.id, words)

    msg = (await db.get_msg('search-commit'))['message']
    msg = msg.replace('{{words}}', '<i>' + words + '</i>')
    await message.answer(msg, reply_markup=menu_markup)
    await Variants.menu.set()
    await update_global_keywords()

    return True


async def stop_words_update(message: types.Message, state: FSMContext):

    words = message.text.strip().lower()
    words = words[:-1] if words and words[-1] == ',' else words
    words = ', '.join(sorted(list(set(list(map(lambda word: word.strip(), words.split(',')))))))
    await db.stop_words_update(message.from_user.id, words)

    msg = (await db.get_msg('stop-commit'))['message']
    msg = msg.replace('{{words}}', '<i>' + words + '</i>')
    await message.answer(msg, reply_markup=menu_markup)
    await Variants.menu.set()

    return True


async def new_message(message: types.Message, state: FSMContext):
    words_rows = await db.get_all_words()
    for item in words_rows:
        data = dict(item)
        if data['search_words'] and check_matches(message.text, data['search_words'].split(', ')):
            if not data['stop_words'] or not check_matches(message.text, data['stop_words'].split(', ')):
                await message.forward(data['user_id'])
                await asyncio.sleep(0.1)
    return True


async def new_message_caption(message: types.Message, state: FSMContext):
    words_rows = await db.get_all_words()
    for item in words_rows:
        data = dict(item)
        if data['search_words'] and check_matches(message.caption, data['search_words'].split(', ')):
            if not data['stop_words'] or not check_matches(message.caption, data['stop_words'].split(', ')):
                await message.forward(data['user_id'])
                await asyncio.sleep(0.1)
    return True


async def links(message: types.Message, state: FSMContext):
    text = message.reply_to_message.text
    text = clear_message(text)
    if hasattr(message.reply_to_message.forward_from_chat, 'title'):
        return False
    sender_name = message.reply_to_message.forward_sender_name
    if not sender_name:
        sender_name = message.reply_to_message.forward_from.first_name
        sender_last_name = message.reply_to_message.forward_from.last_name
        if sender_last_name:
            sender_name += (' ' + sender_last_name)
    d1 = md5(('first' + sender_name + text).encode()).hexdigest()
    d2 = md5(('second' + sender_name + text).encode()).hexdigest()
    username = await db.get_username_by_sign(d1, d2)
    if username and username['sender_username']:
        await message.reply('@' + username['sender_username'])
    else:
        await message.reply((await db.get_msg('no-username'))['message'])
    return

async def handle_MessageCantBeDeleted(*args, **kwargs):
    return True

async def handle_BotBlocked(*args, **kwargs):
    return True