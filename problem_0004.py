def is_palindrome(num):
    return str(num)==str(num)[::-1]

largest = 0
for a in range(100,1000):
    for b in range(1000,100,-1):
        if is_palindrome(a*b) and a*b > largest:
            largest = a*b
            break


print(largest)