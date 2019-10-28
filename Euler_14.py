import time
start_time = time.time()
start = 13
results=[]

memo = {}                               # initialize the memo dictionary
def collatz_seq(n):
    if not n in memo:                   # check if already computed
        if n == 1:                      # if not compute it
            memo[n] = 1                 # cache it
        elif n % 2 == 0:
            memo[n] = collatz_seq(n // 2) + 1
        else:
            memo[n] = collatz_seq(3*n + 1) + 1
    results.append(n)
    return memo[n]                      # and return it
limit = 1000000
max_terms = 10
max_answer = 13
for x in range(int(limit/2), limit):
    #print (x, collatz_seq(x),"iterations")
    if collatz_seq(x) > max_terms:
        max_terms = collatz_seq(x)
        max_answer = x
print (max_answer, max_terms, "iterations")

print('Time:', (time.time() - start_time))