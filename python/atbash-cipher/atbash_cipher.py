import string
import re
try:
    from string import maketrans as mktrans
except ImportError:  # python3
    mktrans = str.maketrans


def maketrans(_from, to, remove):
    """ Creates a translation tuple which is compatible with python 2 and 3.
    When calling str.translate() use the * operator to unpack the tuple.  For
    python 2 This will unpack the translation table and the list of chars to
    remove.  For python 3 the list of chars to remove are in the table and the
    table is the only item in the tuple to unpack.
    """
    try:
        return mktrans(_from, to, remove),
    except TypeError:
        return mktrans(_from, to), remove

remove = string.whitespace + string.punctuation
backwards = string.ascii_lowercase[::-1]
CIPHER = maketrans(string.ascii_letters, backwards * 2, remove)


def add_spaces(ciphered_text):
    return re.sub(r'(.....)', r'\1 ', ciphered_text).strip()


def encode(plain_text):
    encoded = plain_text.translate(*CIPHER)
    return add_spaces(encoded)


def decode(ciphered_text):
    return ciphered_text.translate(*CIPHER)
