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

def closest_weight(x):
    # find the weight of x
    # define weight in, weight out and a variable that's incremented on each loop (difference)

    # check x - diff -> if weight of x = weight of x - diff, return x - diff
    # check x + diff -> if weight of x = weight of x + diff, return x + diff
    # else, if neither is true, increment the difference
    # variables:
    # x, the input
    # the weight of x
    # the weight of the int to be evaluated
    # the difference

    # we need a function to check weights, and a loop to evaluate candidate outputs and increment the difference
    pass