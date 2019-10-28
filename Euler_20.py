import time
import math
start = time.time()

n = 100
digits = []
for step in range (0, len(str(math.factorial(n)))):
    digits.append(str(math.factorial(n))[step])
print(digits)

total = 0
for i in range (0, len(digits)):
    total = total + int(digits[i])

elapsed = time.time() - start
print (total,"found in",elapsed,"seconds.")