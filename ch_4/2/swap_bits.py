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

print(f'Indices {i} and {j} swapped in binary representation of {x}: ', swap_bits1(x, i, j))
