
finished = False
n = 19 # largest prime factor

while not finished:
    n+=19
    for m in range(1,20):
        if n%m != 0:
            finished = False
            break
        else:
            finished = True

print(n)
