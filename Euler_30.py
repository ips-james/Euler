limit = 300000
results = []
for n in range (2, limit):
    total = 0
    for digit in range (0, len(str(n))):
        total = total + int(str(n)[digit])**5
    if total == n:
       results.append(total)

print(results)
print(sum(results))