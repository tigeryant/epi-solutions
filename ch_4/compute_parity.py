import csv
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

# x = 13
# print(f'parity of {x}:', parity3(x))

# initialise x to decimal representation of some 64-bit integer
# x = 17847869031996526993 # parity of 1
x = 7401045055098065760 # parity of 0

# an improvement based on caching results in a lookup table

# initialise pre_pc as the cache read as a list
with open('parity_cache', mode='rb') as parity_cache:
    pre_pc = list(parity_cache.read())

def parity4(x):
    mask_size = 16
    bit_mask = 0xFFFF
    return (pre_pc[x >> (3 * mask_size)] ^
        pre_pc[(x >> (2 * mask_size)) & bit_mask] ^
        pre_pc[(x >> mask_size) & bit_mask] ^
        pre_pc[x & bit_mask])

print(f'parity4 of x: {parity4(x)}')
