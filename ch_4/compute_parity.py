from count_bits import count_bits 

# compute the parity of a 64-bit word
# find the number of bits, return num_bits (the result) mod 2
def compute_parity(x):
    return count_bits(x) % 2

# x = 17
# x = 11111111111511111111

# x = 4
# print(f'parity of {x}:', compute_parity(x))

# compute the parity of a large number of 64-bit words
# brute force - pass an array of 64-bit words, calculating the parity of each using the above method.
# return the result
# hint - use a lookup table

# brute force parity
def parity(x):
    result = 0
    while bool(x):
        result ^= x & 1 # XOR x AND 1
        x >>= 1
    return result

x = 12
print(f'parity of {x}:', compute_parity(x))