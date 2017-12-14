from collections import Counter
import re

def word_count(phrase):
    words = re.split('[^a-z0-9\']+', phrase.lower())
    counter = Counter(w.strip('\'') for w in words)
    # re.split includes empty strings
    del counter['']
    return counter
