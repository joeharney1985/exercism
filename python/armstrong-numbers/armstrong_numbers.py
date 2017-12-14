def is_armstrong(number):
    s = str(number)
    return sum(int(d)**len(str(number)) for d in str(number)) == number
