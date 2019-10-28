def reverse_sum(n):
    return n + int(str(n)[::-1])
sum = 0
answers = 0
limit = 10**7
for x in range (1, limit):
    if x%10 == 0:
        continue
    if all(int(b) % 2 == 1 for b in str(reverse_sum(x))):
        answers += 1

print(answers)