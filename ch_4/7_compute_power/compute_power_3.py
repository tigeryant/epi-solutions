"""
The key to efficiency is to get more work done with each multiplication, thereby using fewer multiplications to accomplish the same result.

If the least significant bit of y is 0, the result is (x^y/2)^2, otherwise, it is x * (x^y/2)^2. This gives a recursive algorithm for 
computing x^y when y is nonnegative.
"""

# solution

def power(x: float, y: int) -> float:
    result, power = 1.0, y
    if y < 0: # handle the case in which y is negative
        power, x = -power, 1.0 / x
    while power:
        if power & 1: # evaluate the bit in the least significant position
            result *= x # either result is multiplied by x...
        x, power = x * x, power >> 1 # or x is squared
    return result

x = 2
y = -13
print(f'{x} raised to the power of {y} = {power(x, y)}')
print(f'The correct answer is: {pow(x, y)}')