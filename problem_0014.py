def collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n +1
    
chains = {}
longest_chain = 1
for num in range(1_000_000):
    chain = 1
    start_num = num
    while num > 1:
        if num in chains:
            chain = chain+chains[num]
            num = 1
        else:
            num = collatz(num)
            chain+=1
    chains[start_num]=chain
    if chain > longest_chain:
        longest_chain = chain
        longest_chain_num = start_num

print(longest_chain_num)