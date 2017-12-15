import math


def multiples_to(limit, base):
    return [base * i for i in range(1, int(math.ceil(limit / float(base))))]


def sum_of_multiples(limit, bases):
    return sum(set([m for b in bases for m in multiples_to(limit, b)]))
