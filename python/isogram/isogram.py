

def is_isogram(string):
    ignore = (' ', '-')
    seen = dict()
    for char in string.lower():
        if char not in ignore and char in seen:
            return False
        seen[char] = True
    return True
