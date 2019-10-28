limit = 10000
total = 0

def sd(n):
    sum_n = 0
    for i in range(1, n):
        if n % i == 0: sum_n += i
    return sum_n

divisors_sum_list =[sd(i) for i in range (1, limit+1)]
print (divisors_sum_list)
for x in range (1, limit):
    if sd(x) > x:
        low = x
        high = sd(x)
    else:
        low = sd(x)
        high = x
    if sd(low) == high and sd(high) == low and low != high:
        print(low, high)
        total = total + low + high

print(total/2)
