from math import sqrt
def sd(n):
    sum_n = 1
    t = sqrt(n)
    for i in range(2, int(t)+1):
        if n % i == 0: sum_n += i + (n/i)
    if t == int(t): sum_n = sum_n -t
    return sum_n

limit = 20161
results = set()
answer = 0
for n in range (1, limit+1):
    if sd(n) > n: results.add(n)
    if not any ((n-a in results) for a in results):
        print (n)
        answer = answer + n

print (answer)