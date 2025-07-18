def is_prime(num):
    if (num == 1) or (num == 2):
        return True
    for n in range(3,int(num**0.5)):
        if is_factor(n, num):
            return False
    return True

def is_factor(num, target):
    return target % num == 0

#target = 13195
target = 600851475143

while not is_prime(target):
    for n in range(2,int(target**0.5)):
        if is_factor(n, target):
            if is_prime(n):
                target /= n
                break
print(target)


