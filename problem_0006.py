squares = 0
sums = 0
for n in range(101):
    squares +=n**2
    sums+=n

print(sums**2-squares)