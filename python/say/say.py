ones = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

bases = {
    3: 'thir',
    4: 'four',
    5: 'fif',
    6: 'six',
    7: 'seven',
    8: 'eigh',
    9: 'nin',
}

teens = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
}
teens.update({10 + k: bases[k] + 'teen' for k in bases})

tens = {
    20: 'twenty',
    30: 'thirty',
}
tens.update({10 * k: bases[k] + 'ty' for k in bases})

scale = [' trillion', ' billion', ' million', ' thousand', '']


def rzip(l1, l2):
    """ Works just like zip but zips from right to left.

    This is important when the len of `l1` does not match the len of `l2`
    """
    return reversed(zip(reversed(l1), reversed(l2)))

def split_on_thousands(big_num):
    return split_on_thousands(big_num / 1000) + [big_num % 1000] if big_num else []


def say(number):
    if number == 0:
        return 'zero'
    if number < 0:
        raise ValueError
    return say_helper(number)


def say_helper(number):
    print number
    if number == 0:
        return 'zero'
    if number in ones:
        return ones[number]
    if number in teens:
        return teens[number]
    if number in tens:
        return tens[number]
    if number < 100:
        return '-'.join([tens[(number / 10) * 10], say_helper(number % 10)])
    if number % 100 == 0:
        return ones[(number / 100)] + ' hundred'
    if number < 1000:
        return ' and '.join([ones[(number / 100)] + ' hundred', say_helper(number % 100)])
    return ' '.join(say_helper(n) + scale if n != 0 else '' for n, scale in rzip(split_on_thousands(number), scale))

if __name__ == '__main__':
    print say(100)
