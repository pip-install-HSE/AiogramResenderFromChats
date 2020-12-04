import re

import config


def load_words(file_path):
  with open(file_path, 'r') as file:
    data = file.read()
  if data:
    return data.lower().strip().split(config.joiner)
  else:
    return None


def check_matches(text, phrases):
  for word in phrases:
    regexp = re.compile(config.pattern.replace("{{phrase}}", word))
    if regexp.search(" " + text.lower() + " "):
      return True
  return False