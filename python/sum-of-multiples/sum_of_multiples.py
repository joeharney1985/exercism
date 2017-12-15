def multiples_to(limit, base):
    multiple = base
    while num < limit:
        yield multiple
        multiple += base

def sum_of_multiples(limit, multiples):
    return sum(sum(multiples_to(limit, m)) for m in multiples)
