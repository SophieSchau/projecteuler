# a**2 + b**2 = c**2, a + b + c = 1000
squares = [x**2 for x in range(1, 1000)]
found = False
for ii, a_square in enumerate(squares):
    for jj, b_square in enumerate(squares[ii:]):
        c_square = a_square+b_square
        if a_square**0.5+b_square**0.5+(c_square)**0.5 == 1000:
            print(int(a_square**0.5*b_square**0.5*(a_square+b_square)**0.5))
            found = True
            break
    if found:
        break
