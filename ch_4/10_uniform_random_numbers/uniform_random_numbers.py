"""
This problem is motivated by the following scenario. Six friends have to select a designated driver using a single unbiased coin.
The process should be fair to everyone.

How would you implement a random number generator that generates a random integer i between a and b, inclusive, given a random number generator that
produces zero or one with equal probability? All values in [a, b] should be equally likely.
"""

import random

# random number generator that produces zero or one with equal probability
def zero_one_random():
    return random.randint(0, 1)

# if x is a power of 2, we could iteratively flip the coin x/2 times. Each time, we split the space in half
# and return the half that is determined by the coin toss (lower or upper half depending on 0 or 1)
# Eventually, we're only left with one number, so we return this number

# How do we deal with the case in which x is not a power of 2?

