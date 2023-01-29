"""
A little math leads to the correct approach. Suppose we flip the bit at index k1 and flip the bit at index k2, k1 > k2. Then the absolute value of the
difference between the original integer and the new one is 2^k1  2^k2. To minimize this, we should make k1 as small as possible and k2 as close to k1.

Since we must preserve the weight, the bit at index k1 has to be different from the bit in k2, otherwise the flips lead to an integer with a different 
weight. This means the smallest k1 is the rightmost bit that's different from the LSB, and k2 must be the very next bit. In summary, the correct
approach is to swap the two rightmost consecutive bits that differ.
"""

# assume all bits are not ones, and that the input is not 0

# iterate over the bits from LSB to MSB
# if the bit to it's right is logically NOT equal to it, swap them and return the result
# if they are equal, move left a bit (increment the position) and retry

def closest_weight(x):
    position = 0

    while True:
        # find the value of the bit at position
        right_bit = (x >> position) & 1
        # find the value of the bit at position + 1
        left_bit = (x >> (position + 1)) & 1
        if right_bit != left_bit:
            # XOR x against a mask of 0x3 (11 in binary) that has been shifted into position
            # XORing against one always gives the inverse - exactly one arg must be one for the output to be one
            mask = 0x3
            positioned_mask = mask << position
            output = x ^ positioned_mask
            return output
        position += 1

x = 7
print(f'Closest weight integer to {x}: {closest_weight(x)}')