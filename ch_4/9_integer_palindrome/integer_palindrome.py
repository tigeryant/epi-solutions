"""
A palindromic string is one which reads the same forwards and backwards, e.g., "redivider". In this problem, you are to write a program which
determines if the decimal representation of an integer is a palindromic string. For example, your program should return true for the inputs
0, 1, 7, 11, 121, 333, and 2147447412, and false for the inputs -1, 12, 100, and 2147483647.

Write a program that takes an integer and determines if that integer's representation as a decimal string is a palindrome.
"""

# return false if x < 0
# use the solution from the last exercise, then check if x and reversed_x are equivalent
# if they are, return true, else false

def integer_palindrome(x: int) -> bool:
    if x < 0:
        return False
    
    x_reversed = reverse(x)
    if x == x_reversed:
        return True
    return False

def reverse(x: int) -> int:
    result, x_remaining = 0, abs(x)
    while x_remaining:
        # make room for the new digit (like a left shift), then add x_remaining mod 10 to it
        result = result * 10 + x_remaining % 10
        # divide x_remaining by 10 (effectively like a right shift)
        x_remaining //= 10
    return result

# another way is if we iterate from both ends and fail as soon as there's a mismatch

x = 2147447412
# x = -3239
# x = 121
print(f'True if x is a palindrome, False if not: {integer_palindrome(x)}')
