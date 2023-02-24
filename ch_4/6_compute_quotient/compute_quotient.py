'''
Compute quotient without arithmetical operators

Given two positive integers, compute their quotient, using only the addition, subtraction and shifting operators
'''

# brute force

def divide_brute_force(x, y):
    # iteratively subtract y from x
    # each iteration, we increment the quotient
    # each iteration we also check the result

    # refactor
    remainder = x - y
    if remainder < 0:
        return 0
    if remainder == 0:
        return 1

    quotient = 0
    while remainder >= 0:
        remainder = remainder - y
        quotient += 1
    return quotient

x = 24
y = 6
print(f'The quotient derived from dividing {x} by {y} is {divide_brute_force(x, y)}')

