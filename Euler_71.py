import pprint
def computeHCF(x, y):

   # This function implements the Euclidian algorithm to find H.C.F. of two numbers
   while y:
       x, y = y, x % y

   return x

def take_third(elem):
    return elem[2]



limit_d = 8
aim = 3/7

target_range = int(limit_d * aim)

results = []
for d in range (1 , limit_d + 1, 1):
    for n in range (1, d):
        if computeHCF(n, d) == 1:
            results.append([n,d,n/d])

sorted_results = sorted(results,key=take_third)
pprint.pprint(sorted_results)
print(len(results))
print(aim,"is at index",sorted_results.index([3,7,3/7]))
print("The value to the left of",aim,"is",sorted_results[sorted_results.index([3,7,3/7])-1])