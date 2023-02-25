'''
Compute quotient without arithmetical operators

Given two positive integers, compute their quotient, using only the addition, subtraction and shifting operators
'''

# solution

def divide(x, y):
    result, power = 0, 32
    y_power = y << power
    while x >= y:
        while y_power > x: # here we decrease 2^k*y and power until it's smaller than x
            y_power >>= 1 # left shift 2^k*y by 1
            power -= 1 # decrement k

        result += 1 << power # add 2^k to the quotient
        x -= y_power # subtract 2^k*y from x
    return result

x = 293842837498237498238947
y = 23894293874983
# x = 2
# y = 2
print(f'The quotient when dividing {x} by {y} = {divide(x, y)}')
print(f'The correct answer is {x // y}')
