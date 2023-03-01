"""
We can avoid the O(n) space complexity used by the string representation by directly extracting the digits from the input. The number of digits,
n, in the input's string representation is the log (base 10) of the input value, x. To be precise, n = floor(log10 * x) + 1. Therefore, the least significant
digit is x mod 10, and the most significant digit is x/10^n-1.
"""

# solution

import math

def is_palindrome_number(x: int) -> bool:
    if x <= 0:
        return x == 0
    
    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10**(num_digits - 1)
    for _ in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False 
        x %= msd_mask # Remove the most significant digit of x.
        x //= 10 # Remove the least significant digit of x.
        msd_mask //= 100
    return True

x = 2147447412
# x = -3239
# x = 121
print(f'True if x is a palindrome, False if not: {is_palindrome_number(x)}')
