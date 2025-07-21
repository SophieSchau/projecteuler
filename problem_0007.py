def is_prime(num):
    if (num == 1):
        return False
    if (num == 2):
        return True
    for n in range(2,int(num**0.5)+1):
        if num%n == 0:
            return False
    return True

n = 0
num = 1
while n < 10_001:
    num+=1
    if is_prime(num):
        n+=1
        print(n, num)


print(num)
