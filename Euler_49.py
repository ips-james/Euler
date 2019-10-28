from itertools import permutations
from sieve import sieve


primes = sieve(1488, 9999)


def check(prime_list):
    for i in range(len(prime_list)):
        for j in range (i+1, len(prime_list)):
            k = (prime_list[j] + (prime_list[j] - prime_list[i]))
            if k in prime_list:
                return str(prime_list[i]) + str(prime_list[j]) + str(k)


for n in primes:
    p = permutations(str(n))
    a = [int(''.join(x)) for x in p]
    a = list(set([x for x in a if x in primes]))
    a.sort()
    if len(a) >= 3:
        if check(a):
            print (check(a))
            break