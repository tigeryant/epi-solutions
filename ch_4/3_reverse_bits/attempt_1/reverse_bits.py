"""
Write a program that takes a 64-bit unsigned integer and returns the 64-bit unsigned integer consisting of the bits in reverse order. For example,
if the input is (1110000000000001), the output should be (1000000000000111). Hint: Use a lookup table
"""

# We can create a lookup table/cache containing all possible reversed 16-bit segments, indexed from 0 to 65535
# We then split the 64-bit integer, call it x, into 4 segments, indexed from 0 to 3.

# We take segment 0, use it as an index in our cache, and find the reversed word
# We store this word in our new 64-bit word at index 3
# We do the same for the other segments, mapping the old segment indices to the new as follows:
# 1 -> 2
# 2 -> 1
# 3 -> 0

# We join the new segments together and return it as a single 64-bit int

# INITIALISING THE CACHE
# See init_cache.py

x = 3407369155461708992 # reversed: 234001936739111668
# x = 8123010520786304973 # reversed: 12969905612457336078

def reverse_bits1(x):
    return int('{:064b}'.format(x)[::-1], 2)
    # converts x to binary, pads with up to 64 leading zeros, the entire value is sliced in reverse order, 2 is the base passed to the int method
    # see this on stackoverflow: https://stackoverflow.com/questions/12681945/reversing-bits-of-python-integer

print('reversed 64-bit int: ', reverse_bits1(x))