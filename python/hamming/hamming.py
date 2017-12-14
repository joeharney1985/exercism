def distance(strand_a, strand_b):
    if not len(strand_a) == len(strand_b):
        raise ValueError
    return sum([1 if a != b else 0 for a, b in zip(strand_a, strand_b)])
