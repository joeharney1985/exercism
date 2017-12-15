import re


def abbreviate(words):
    return re.sub(r'(\w)\w*\W*', r'\1', words.upper())
