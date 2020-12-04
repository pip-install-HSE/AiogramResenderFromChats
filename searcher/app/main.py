from telethon import TelegramClient, events
from telethon.tl.types import User, Channel
import re
import asyncio
import logging

from globals import Parser
from database import Database

import config


logging.basicConfig(level=logging.INFO)

db = Database()

parser = Parser(db)
parser.load()

client = TelegramClient(config.api_sess_name,
                        config.api_id,
                        config.api_hash)


@client.on(events.NewMessage(func=lambda event: not event.is_private)) # do not search in private messages
async def push_matched_message(event):

  chat_id = event.chat_id
  text = event.message.message

  # check chat
  if chat_id in config.ignore_chats:
    return False

  # check for stop words
  if parser.stopwords and parser.check_matches(text, parser.stopwords):
    return False

  # check for keywords
  if parser.keywords and parser.check_matches(text, parser.keywords):
    parser.add_event(event)
  
  return True


async def updater():
  #print(await db.get_all_words())
  while True:
    parser.load()
    #print(parser.keywords)
    await asyncio.sleep(2.5)


async def forwarder():
 
  while True:
 
    if parser.events:
  
      event = parser.get_event()
      sender = await event.get_sender()
      username = None
      name = ''
      
      if isinstance(sender, User):
        name = sender.first_name if sender.first_name else ''
        name += (' ' + sender.last_name) if sender.last_name else ''
        username = sender.username

      '''
      if isinstance(sender, Channel):
        name = sender.title
      '''

      logging.info('SIGN\n' + event.message.message)
      s1, s2 = parser.sign(event.message.message, name)
      res = await db.check_sign(s1, s2)

      if res:
        continue

      res = await db.add_sign(s1, s2, name, username)

      # forward
      try:
        target_chat = await client.get_entity(config.target_chat_id) # Group to send messages matched
        res = await event.forward_to(target_chat)
      except Exception as e:
        pass

      #print(event, entity, sender, sep='\n\n')
    
    await asyncio.sleep(0.5)


with client:
  client.loop.create_task(updater())
  client.loop.create_task(forwarder())
  client.run_until_disconnected()