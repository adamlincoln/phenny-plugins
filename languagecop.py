import re
from copy import deepcopy

word_length_forbidden = 4

pattern = re.compile(r'[^\w\s]+')

def check_for_word_of_length(phenny, inp):
   print inp
   stripped_words = pattern.sub('', inp)
   print stripped_words
   for word in stripped_words.split():
      if len(word) == word_length_forbidden:
         phenny.say(inp.nick + ': YOU VIOLATOR!  You uttered ' + word + '.')

check_for_word_of_length.rule = r'(.*)'
check_for_word_of_length.thread = False

