test_limit = 400
lower_bound = 150

limit = 80000
triangle_array = []
pent_array = []
hex_array = []

def is_triangle(n):
    for x in range(lower_bound,test_limit):
        triangle_array.append((x/2)*(x+1))
    return n in triangle_array

def is_pent(n):
    for y in range(lower_bound,test_limit):
        pent_array.append((y/2)*((3*y)-1))
    return n in pent_array

def is_hex(n):
    for z in range(lower_bound,test_limit):
        hex_array.append(z*((2*z)-1))
    return n in hex_array

for x in range (40000, limit):
    if is_pent(x) and is_hex(x):
        print(x)