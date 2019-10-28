lower = 1
top = 150
test_range = range (120, top+1,2)
solutions = []

def test(p):
    hit = 0
    for c in range (int(p/2),lower,-1):
        for b in range (c, lower,-1):
            for a in range (lower,int(p/(2+(2**0.5)))):
                print(p,c, b)
                if a**2 + b**2 == c**2 and a + b + c == p:
                    hit = hit + 1
    return hit

max_num = 1
best_num = 1
for num in test_range:

    if test(num) > max_num:

        max_num = test(num)
        best_num = num

print (best_num, max_num)


