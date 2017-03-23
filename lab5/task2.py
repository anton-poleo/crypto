from hashlib import sha1
def continued_fraction(e, n):
    while n:
        a = e // n
        yield  a
        e, n = n, e - a*n

def convergents(cont_frac):
    prev_q, q = 1, 0
    for x in cont_frac:
        prev_q, q = q, x*q + prev_q
        yield q

def is_exp(e, n, d):
    some_M = 123
    some_C = pow(some_M, e, n)
    return  some_M == pow(some_C, d, n)

def winner_attack(e, n):
    frac_denominators = list(convergents(continued_fraction(e, n)))
    print(frac_denominators)
    for i in range(len(frac_denominators)):
        if is_exp(e, n, frac_denominators[i]):
            print("Valid exp = ", frac_denominators[i])
            return frac_denominators[i]
isE = 13681819998357386977436324075307033163
isN = 75847237140497703430428347287960403177
a = winner_attack(isE, isN)

print(sha1(str(a).encode()).hexdigest())
