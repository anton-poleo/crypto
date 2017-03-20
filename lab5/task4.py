from math import sqrt
n = 328542140867
def divisor(value):
    return n % value == 0
def factorization():
    factor = 2
    while not divisor(factor):
        factor += 1
    return factor, int(n/factor)
a, b = factorization()
print(a, b, a*b)
