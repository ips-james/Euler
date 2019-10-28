def prime_test(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    root_n = int(round(n ** 0.5))
    for divisor in range(2, root_n + 1):
        if n % divisor == 0:
            return False
    return True


testValue = 10000

result = []


def count_primes_in_range():
    for i in range(1000, testValue, 1):
        if prime_test(i):
            result.append(i)

    print("Found", len(result), "primes.")
