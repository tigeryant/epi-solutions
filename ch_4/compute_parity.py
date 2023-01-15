from count_bits import count_bits 

# compute the parity of a 64-bit word
# find the number of bits, return num_bits (the result) mod 2
def parity1(x):
    return count_bits(x) % 2

# x = 17
# x = 11111111111511111111

# x = 4
# print(f'parity of {x}:', parity1(x))

# compute the parity of a large number of 64-bit words
# brute force - pass an array of 64-bit words, calculating the parity of each using the above method.
# return the result
# hint - use a lookup table

# brute force parity
def parity2(x):
    result = 0
    while bool(x):
        result ^= x & 1 # XOR x AND 1
        x >>= 1 # right shift x
    return result

# x = 12
# print(f'parity of {x}:', parity2(x))

# an improvement based on a bit manipulation trick which erases the lowest set bit in a word

def parity3(x):
    result = 0
    while bool(x):
        result ^= 1 # XOR the result with 1
        x &= x -1 # erase the lowest set bit of x
    return result

x = 13
print(f'parity of {x}:', parity3(x))

# an improvement based on caching results in a lookup table

def parity4(x):
    mask_size = 16
    bit_mask = 0xFFFF
    return (PRE_PC[x >> (3 * mask_size)] ^
        PRE_PC[(x >> (2 * mask_size)) & bit_mask] ^
        PRE_PC[(x >> mask_size) & bit_mask] ^
        PRE_PC[x & bit_mask])

# TODO compute PRE_PC using one of the above methods, then use it as the cache in this version
# PRE_PC is precomputed parity cache