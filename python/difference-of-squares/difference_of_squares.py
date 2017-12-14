def square_of_sum(N):
    return sum(int(n) for n in range(1, N + 1)) ** 2


def sum_of_squares(N):
    return sum(int(n) ** 2 for n in range(1, N + 1))


def difference(N):
    return square_of_sum(N) - sum_of_squares(N)
