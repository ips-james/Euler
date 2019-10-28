def palindrome(n):
    return str(n) == str(n)[::-1]

def find_max_palindrome(min=1000, max=9999):
    max_palindrome = 0

    for a in range(min, max + 1):
        for b in range(a + 1, max + 1):  # avoid duplicates
            prod = a * b
            if prod > max_palindrome and palindrome(prod):
                max_palindrome = prod
                final_a = a
                final_b = b
    return max_palindrome, final_a, final_b

print ("found", str(find_max_palindrome()))