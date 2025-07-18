def fibonacci(seq):
    next = [seq[-1], seq[-2]+seq[-1]]
    return next


fib = [1,1]
idx = 2
while len(str(fib[-1]))<1000:
    idx+=1
    fib = fibonacci(fib)

print(idx)
