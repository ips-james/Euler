import math
limit = 1000000
answer = 0
for num in range (10, limit+1):
    sum = 0
    for x in range (0, len(str(num))):
        sum = sum + math.factorial(int(str(num)[x]))
    if num == sum:
        answer = answer + num
        print (num, sum)
print (answer)
