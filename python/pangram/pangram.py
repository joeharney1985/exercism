def is_pangram(sentence):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    sentence = sentence.lower()
    return all(c in sentence for c in ALPHABET)
