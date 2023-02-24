'''
Compute quotient without arithmetical operators

Given two positive integers, compute their quotient, using only the addition, subtraction and shifting operators
'''

# solution

def divide(x, y):
    result, power = 0, 32
    y_power = y << power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1

        result += 1 << power
        x -= y_power
    return result

x = 293842837498237498238947
y = 23894293874983
# x = 2
# y = 2
print(f'The quotient when dividing {x} by {y} = {divide(x, y)}')
print(f'The correct answer is {x // y}')
