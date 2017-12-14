import string


def rot_char(c, key):
    if c not in string.ascii_letters:
        return c
    offset = ord('a') if c.islower() else ord('A')
    return chr((ord(c) - offset + key) % 26 + offset)


def rotate(text, key):
    return ''.join(rot_char(c, key) for c in text)
