def sum_of_multiples(limit, bases):
    return sum(set([m for b in bases for m in range(b, limit, b)]))
