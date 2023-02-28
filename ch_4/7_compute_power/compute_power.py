"""
Write a program that takes a double x and an integer y and returns x^y. You can ignore overflow and underflow.
"""

# brute force

def compute_power(x: float, y: int) -> float:
    if y == 0:
        return 1
    if y == 1:
        return x
    
    result = x
    for _ in range(y - 1):
        result *= x
    return result

x = 2.23432
y = 3
print(f'{x} raised to the power of {y} = {compute_power(x, y)}')
print(f'The correct answer is: {pow(x, y)}')