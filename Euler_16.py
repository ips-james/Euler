def sum_digits(n):
    total = [int (d) for d in str(n)]

    return sum(total)

n= input ("Enter a number")
print(2**int(n))
print(sum_digits(2**int(n)))