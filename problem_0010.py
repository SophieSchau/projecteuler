def is_prime(num):
    for n in range(2,int(num**0.5)+1):
        if num % n == 0:
            return False
    return True

total = 2
for ii in range(3,int(2e6),2):
    if is_prime(ii):
        total+=ii

print(total)