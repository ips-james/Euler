n1 = 1
results = [1]
limit = 10000
digits = 999
for n in range (1,limit):
    results.append(n1)
    n1 = n1 + results[n-1]
    if len(str(results[n])) > digits:
        print(results[n])
        print("Index", n+1)
        exit()

