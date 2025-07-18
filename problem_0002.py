def fibonacci(seq):
    next = [seq[-1], seq[-2]+seq[-1]]
    return next


fib = [1,2]
total = 2

while fib[-1] < 4e6:
    fib = fibonacci(fib)
    if fib[-1]%2 == 0:
        total+=fib[-1]

print(total)