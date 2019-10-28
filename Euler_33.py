results = []
test_range = range(10,100)
final_numerator = 1
final_denominator = 1
for denominator in test_range:
    for numerator in range (11, denominator - 1):
        if numerator%10 ==0:
            continue
        if denominator%10 ==0:
            continue
        if str(numerator)[1] == str(denominator)[0]:
            if numerator / denominator == int(str(numerator)[0]) / int(str(denominator)[1]):
                results.append([numerator,denominator])
                final_numerator = final_numerator * numerator
                final_denominator = final_denominator * denominator

print(results)
print(final_numerator)
print(final_denominator)

