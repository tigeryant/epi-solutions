def count_bits(x):
    num_bits = 0
    while bool(x):
        num_bits += x & 1 # increments num_bits if least significant bit of x is 0
        x >>= 1 # right shifts x
    return num_bits

# print(count_bits(2))

# print('9 & 1 ', 9 & 1)
# print('10 & 1 ', 10 & 1)
# print('3 & 1 ', 3 & 1)
# print('4 & 1 ', 4 & 1)