import string
import re
try:
    from string import maketrans
except ImportError:
    maketans = str.maketrans


CIPHER = maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])
remove = string.whitespace + string.punctuation


def add_spaces(ciphered_text):
    return re.sub(r'(.....)', r'\1 ', ciphered_text).strip()


def encode(plain_text):
    return add_spaces(plain_text.lower().translate(CIPHER, remove))


def decode(ciphered_text):
    return ciphered_text.lower().translate(CIPHER, remove)
