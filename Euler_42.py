text_file = open("C:/Users/James/Documents/Personal/Data Analysis/Python/p042_words.txt", "r")
lines = text_file.read().split(',')
sums_array = []
triangle_array = []
limit = 20

def is_triangle(n):
    for x in range(1,limit):
        triangle_array.append((x/2)*(x+1))
    return n in triangle_array


count=0
for line_num in range(0, len(lines)):
    sum = 0
    for char in lines[line_num]:
        sum = sum + (ord(char)-64)
    if is_triangle(sum):
        count = count + 1

print(count)
print(triangle_array)
#max word value is 192