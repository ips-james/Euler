def genfact(a):
    t = []
    for i in range(1, int(a**0.5)+1):
        if a%i == 0:
            t.append(i)
            t.append(int(a/i))
            t.sort()
    return t

#create array of triangular numbers
limit = 800000000
triangles = []
triangles.append(1)

for n in range(1,int(round(limit ** 0.5)),1):
    triangles.append (triangles[n-1] + (n+1))

divisors = []
for x in triangles:
        if len(genfact(x)) > 500:
            print (x)
            print(genfact(x))
            exit()