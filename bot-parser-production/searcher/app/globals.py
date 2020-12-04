from hashlib import md5
import re

import config


class Parser():


  def __init__(self, db):
    self.db = db
    self.keywords = None
    self.stopwords = None
    self.events = []


  def load(self):
    self.keywords = self.load_words(config.keywords_file)
    self.stopwords = self.load_words(config.stopwords_file)


  def get_event(self):
    if self.events:
      return self.events.pop(0)


  def add_event(self, event):
    self.events += [event]


  @staticmethod
  def clear_message(message):
    message = message.strip().lower()
    message = re.sub('#[а-яa-z0-9-_]+', '', message)
    message = re.sub('\s+', '', message)
    message = re.sub('[^a-zа-яёїієґ_-]', '', message)
    return message


  @staticmethod
  def sign(message, sender_name):
    message = Parser.clear_message(message)
    d1 = md5(('first' + sender_name + message).encode()).hexdigest()
    d2 = md5(('second' + sender_name + message).encode()).hexdigest()
    return (d1, d2)


  @staticmethod
  def load_words(file_path):
    with open(file_path, 'r') as file:
      data = file.read()
    if data:
      return data.lower().strip().split(config.joiner)
    else:
      return None


  @staticmethod
  def check_matches(text, phrases):
    for word in phrases:
      regexp = re.compile(config.pattern.replace("{{phrase}}", re.escape(word)))
      if regexp.search(" " + text.lower() + " "):
        return True
    return False