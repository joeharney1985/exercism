import collections


def is_anagram(w1, w2):
    return collections.Counter(w1) == collections.Counter(w2) and w1 != w2


def detect_anagrams(word, candidates):
    return [c for c in candidates if is_anagram(word.lower(), c.lower())]
