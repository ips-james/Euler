limit = 100

r = range (2, limit+1)
print (len({a**b for a in r for b in r}))
