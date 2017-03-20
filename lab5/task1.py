'''x = 165465489465455564
print(int(x**0.5)**2)
print(x*x)'''
#from math import sqrt
from math import floor, sqrt
#from decimal import Decimal
#import decimal
#decimal.getcontext( ).prec = 10
def sqrt1(x):
    s = round(x ** 0.5)
    return (x - s**2) // (2 * s) + s

def int_number(value):
    return round(value) == value
def method_of_fermat(n):
    x = sqrt1(n) + 1
    while not int_number(sqrt(x**2 - n)):
        x += 1
    y = sqrt1(x ** 2 - n)
    p = x - y
    q = x + y
    return p, q


def gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcd(b, a % b)
        return d, y, x - y * (a // b)


n = 850706101864878999620919880021817869
v = 1864878999620919880022583417
s = 1864878999620919880021831323
e = 811
def rsa_private_key(n, e):
    p, q = method_of_fermat(n)
    euler_func = (p - 1) * (q - 1)
    gcd_tuple = gcd(e, euler_func)
    if(gcd_tuple[0]==1):
        d = gcd_tuple[1] % euler_func
        return d
    else:
        print("Числа не взаимнопростые. НОД = ", gcd_tuple[0])
print(rsa_private_key(n, e))
a, b = method_of_fermat(n)
#print(a, b)
print(int(a*b))