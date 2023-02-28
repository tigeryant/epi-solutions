"""
Write a program which takes an integer and returns the integer corresponding to the digits of the input written in reverse order. For example,
the reverse of 42 is 24, and the reverse of -314 is -413.

------------------------------------

Let the input be k. If k >= 0, then k mod 10 is the most significant digit of the result and the subsequent digits are the reverse of k/10. Supposing
we are to reverse 1132, we iteratively update the result and the input as 2 and 113, then 23 and 11, then 231 and 1, then 2311.

For general k, we record its sign, solve the problem for |k|, and apply the sign to the result.
"""

# solution

def reverse(x: int) -> int:
    result, x_remaining = 0, abs(x)
    while x_remaining:
        # make room for the new digit (like a left shift), then add x_remaining mod 10 to it
        result = result * 10 + x_remaining % 10
        # divide x_remaining by 10 (effectively like a right shift)
        x_remaining //= 10
    return -result if x < 0 else result # adjust the sign if needs be

x = 1132
print(f'The reverse of {x} is {reverse(x)}')