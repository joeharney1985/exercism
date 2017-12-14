from collections import deque


def sieve(limit):
    potential = deque(range(2, limit + 1))
    primes = []
    while len(potential) > 0:
        prime = potential.popleft()
        primes.append(prime)
        multiple = 2 * prime
        while multiple <= limit:
            try:
                potential.remove(multiple)
            except ValueError:
                pass
            multiple += prime
    return primes
