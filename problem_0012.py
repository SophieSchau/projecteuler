def triangle_num(idx):
    num = sum(range(idx+1))
    return num

def num_factors_triangle(num):
    ii = 0
    for n in range(1,int(num**0.5)+1):
        if num % n == 0:
            ii+=1
    
    return ii*2

n = 1
while num_factors_triangle(triangle_num(n)) < 500:
    n+=1

print(triangle_num(n))