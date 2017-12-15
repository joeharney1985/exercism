import re


def abbreviate(words):
    return re.sub(r'\W*(\w)\w*\W*', r'\1', words.upper())
