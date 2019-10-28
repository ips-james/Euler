limit = 100

results = 0
def step(x, memo={1:1, 89:89}):
    if x == 1:
        return 1
    if x == 89:
        return 89
    else:
        next == sum([int(d)**2 for d in str(x)])
        return step(next)


for i in range(1, limit):
    print (i, step(i))

