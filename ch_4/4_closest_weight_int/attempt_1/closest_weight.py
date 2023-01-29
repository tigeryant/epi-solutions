"""
Define the weight of a nonnegative integer x to be the number of bits that are set to 1 in its binary representation.
For example, since 92 in base-2 equals (1011100)sub2, the weight of 92 is 4.

Write a program which takes as input a nonnegative integer x and returns a number y which is not equal to x,
but has the same weight as x and their difference, |y - x|, is as small as possible. You can assume x is not 0, or all 1s.
For example, if x = 6, you should return 5. You can assume the integer fits in 64 bits.

Hint: Start with the least significant bit.
"""

# brute force:
# check the weight of the input.
# compare this weight to the weight of input - 1, input + 1, input - 2, input + 2 etc until a solution is found

def weight(x):
    count = 0
    while x != 0:
        count += 1
        x = x &(x - 1)
    return count

def closest_weight(x):
    diff = 1
    input_weight = weight(x)

    while True:
        current_int = x - diff
        if weight(current_int) is input_weight:
            return current_int
        current_int = x + diff
        if weight(current_int) is input_weight:
            return current_int
        diff += 1

x = 99886623234
print(f'Closest integer by weight to {x}: {closest_weight(x)}')