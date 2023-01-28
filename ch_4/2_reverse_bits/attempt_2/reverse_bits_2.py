"""
Write a program that takes a 64-bit unsigned integer and returns the 64-bit unsigned integer consisting of the bits in reverse order. For example,
if the input is (1110000000000001), the output should be (1000000000000111). Hint: Use a lookup table
"""

# example 64 bit integers
# x = 3407369155461708992 # reversed: 234001936739111668
# x = 8123010520786304973 # reversed: 12969905612457336078
# x = 57717
# x = 1891285767
x = 28858
# x = 47879
# x = 63034
# x = 32717
# x = 8123010520786304973

# note that the maximum value of x for a 16-bit integer is 65535, since 2^16 - 1 = 65535

def reverse_bits(x, size): # pass x and the number of bits representing that integer
    # size = 64 # initialise this to the number of bits in the integer
    position = size - 1
    y = 0
    while position >= 0:
        y |= (x & 1) << position # y equals OR of y and (the extracted LSB leftshifted by position). The OR builds on y without affecting the other bits
        x >>= 1 # set x equal to itself rightshifted by a single bit
        position -= 1 # decrement position by 1
    return y

# print('reversed 64-bit int: ', reverse_bits(x, 64))
print('reversed int: ', reverse_bits(x, 16)) # 16 bit int
# print('reversed int: ', reverse_bits(x, 64)) # 64 bit int

# NOTES
# We extract the lowest bit from x and rightshift it into position.
# We continue this method, but on each iteration we decrement position, while still extracting the LSB.
# This continual process of extracting the LSB and rightshifting x gives us the reverse of x.