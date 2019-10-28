import math


def sieve(start, end):
    arr_prime = [True for i in range(end + 1)]
    divisor = 2
    limit = int(math.sqrt(end))
    for a in range(2, limit + 1):
        if arr_prime[a]:
            for i in range(divisor * 2, end + 1, divisor):
                arr_prime[i] = False
        divisor += 1
    arr_prime[0] = False
    arr_prime[1] = False

    results = []
    for p in range(start, end + 1):
        if arr_prime[p]:

            results.append(p)
    return results



