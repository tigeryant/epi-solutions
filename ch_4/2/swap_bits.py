"""
A 64-bit integer can be viewed as an array of 64 bits, with the bit at index 0 corresponding to the least significant bit (LSB) and the bit at index 63
corresponding to the most significant bit (MSB). Implement code that takes as input a 64-bit integer and swaps the bits at indices i and j.
Hint: When is the swap necessary?
"""

# initial attempt

# thinking about the hint - the swap is only necessary if the bits are not equal
# input a 64 bit integer
# find the value of the bit at index i. if they are equal, return x
# else, change i to its complement, and change j to its complement

# note that there is probably a bit manipulation trick that can come into use here

# x = 17847869031996526993 # parity of 1

# assumes that 0 < i, j < l, where l is ((the number of bits in the binary representation of x) minus 1)

x = 73
i = 1
j = 6

def swap_bits1(x, i, j):
    # convert x to bitfield
    bitlist = [x >> i & 1 for i in range(0, x.bit_length())]

    # compare bits at indeces i and j
    if bitlist[i] is not bitlist[j]:
        # swap the bits
        temp_i = bitlist[i]
        bitlist[i] = bitlist[j]
        bitlist[j] = temp_i

        # return bitlist converted back to int
        swapped = 0
        for bit in reversed(bitlist):
            swapped = (swapped << 1) | bit
        return swapped

    return x

# print(f'1. Indices {i} and {j} swapped in binary representation of {x}: ', swap_bits1(x, i, j))

# attempt 2

# find and isolate x[i] by right shifting x by i, then masking it (& against 0xF)
# do the same for x[j]

# find the result of their XOR, e.g:
# xor = a ^ b
# shift a and b back into position by leftshifting and ORing them
# XOR this with the original x. Return the result

# incorrect, good try

# def swap_bits2(x, i, j):
#     a = (x >> i) & 0x1
#     b = (x >> j) & 0x1

#     if a != b:
#         c = a ^ b
#         a_inverse = a ^ c
#         b_inverse = b ^ c
#         ab_positioned = (a_inverse << i) | (b_inverse << j)
#         swapped = x ^ ab_positioned
#         return swapped

#     return x

# print(f'2. Indices {i} and {j} swapped in binary representation of {x}: ', swap_bits2(x, i, j))

# solution

def swap_bits3(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1: # if the bits are not equal
        bit_mask = (1 << i) | (1 << j) # define the bit mask as the OR of the the mask of the bits at indices i and j
        x ^= bit_mask # x = the XOR of the original x and the bitmask
    return x

print(f'3. Indices {i} and {j} swapped in binary representation of {x}: ', swap_bits3(x, i, j))

# key points: when we XOR against the bitmask, we effectively invert the bit(s) covered by the mask

# steps:
# if the bits are not equal:
# define the bitmask to cover the indices of i and j
# return the xor of x (the original), and the bitmask

# another attempt:

def swap_bits4(x, i, j):
    if ((x >> i) & 1) != ((x >> j) & 1):
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x

print('swap bits 4: ', swap_bits4(x, i, j))