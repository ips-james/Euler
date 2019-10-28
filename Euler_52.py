def num_digits(n):
   l = []
   for char in range(0,len(str(n))):
       l.append(str(n)[char])
   l.sort()
   return l

test = 1
while True:
    if num_digits(test) == num_digits(2*test) == num_digits(3*test) == num_digits(4*test) == num_digits(5*test) == num_digits(6*test):
        print(test, 2*test, 3*test, 4*test, 5*test, 6*test)
        break
    test = test + 1