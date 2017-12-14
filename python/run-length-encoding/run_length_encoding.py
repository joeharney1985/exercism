import re


def encode(string):
    def enc(s):
        return s if len(s) == 1 else str(len(s)) + s[0]
    return ''.join(enc(''.join(m)) for m in re.findall(r'(.)(\1*)', string))


def decode(string):
    def dec(n_repititions, char):
        return char if n_repititions == '' else char * int(n_repititions)
    return ''.join(dec(*m) for m in re.findall(r'(\d*)([a-zA-z ])', string))
