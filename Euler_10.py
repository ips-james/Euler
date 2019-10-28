limit = 2000000
crosslimit = int(limit**0.5) +1
sieve = [True] * (limit)

for even in range (4, limit, 2):
    sieve[even] = False
for n in range (3, crosslimit,2):
    if sieve[n]:
       for m in range (n*n, limit, 2*n):
           sieve[m] = False
results = []
sum = 0
for n in range (2, limit):
    if sieve[n]:
        results.append(n)
        sum = sum + n
print(results)
print(sum)
print (len(results))
print(len(sieve))
