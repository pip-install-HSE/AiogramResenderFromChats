import re

from core import db, bot
import config


async def send_video(uid, file_name):
    file = await db.get_file_id(file_name)
    if file:
        res = await bot.send_video(uid, file['file_id'], caption=None)
    else:
        with open(config.SHARED_FILES + file_name, 'rb') as document:
            res = await bot.send_video(uid, document, caption=None)
            res_save = await db.add_file(file_name, res.video['file_id'])

    return True


async def update_global_keywords():
    keywords = set()
    words = await db.get_all_words()
    for item in words:
        data = dict(item)
        if data['search_words']:
            keywords.update(data['search_words'].split(', '))
    with open(config.SHARED_FOLDER + 'keywords.txt', 'w') as file:
        file.write(', '.join(list(keywords)))
    return True


def check_matches(text, phrases):
    for word in phrases:
        regexp = re.compile(config.PATTERN.replace("{{phrase}}", re.escape(word)))
        if regexp.search(" " + text.lower() + " "):
            return True
    return False


def clear_message(message):
    message = message.strip().lower()
    message = re.sub('#[а-яa-z0-9-_]+', '', message)
    message = re.sub('\s+', '', message)
    message = re.sub('[^a-zа-яёїієґ_-]', '', message)
    return message