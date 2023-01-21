# Now the cache is created, we can use it as a lookup table for the reverse of 16-bit integers
# which form the 4 partitions of a 64-bit integer.

# Take the first 16 bits of x
# find its inverse by using it as the index to the cache (that is, return the value found in the cache at that line)
# map it to the last 16 bits of y (y being the return value, the result of reversing the 64-bit integer)
# continue mapping each 16 bit segment as follows:
# 0 -> 3
# 1 -> 2
# 2 -> 1
# 3 -> 0

# example 64 bit integers
# x = 3407369155461708992 # reversed: 234001936739111668 # in binary (not reversed) 10111101001001011010000011000110100001111010101111110011000000 # 62 bits
x = 8123010520786304973 # reversed: 12969905612457336078 # in binary (not reversed) 0111000010111010101110110000011111110110001110100111111111001101 # leading 0 has been added to make 64 bits
# correct repr of segment_0: 0111000010111010 # in decimal: 28858 # reversed: 23822
# segment_0: 0111000010111010
# segment_1: 1011101100000111 # in decimal: 47879 # reversed: 57565
# first 16 bits 1110000101110101 # in decimal: 57717 # reversed: 44679 # NOTE this binary is missing a leading (MSB) zero!
# first 32 bits 1110000101110101011101100000111 # in decimal 1891285767 # reversed 57565

# rev1 to binary = 1110000011011101
# rev0 to binary = 101110100001110

# importing the cache
with open('reverse_cache.txt', mode='r') as reverse_cache:
    # read each line, append it to the cache_list
    cache_list = reverse_cache.readlines()

# convert cache_list to list of integers
cache_list = [int(x) for x in cache_list]

# TODO fix the issue with the leading zero of a 64 bit integer being ignored

def reverse_bits_with_cache(x):
    bit_mask = 0xFFFF

    # find the first 16 bits of x
    segment_0 = x >> 48
    # print('segment_0: ', segment_0)
    reverse_0 = cache_list[segment_0]
    print('reverse_0: ', reverse_0)
    # find the second 16 bits of x
    segment_1 = (x >> 32) & bit_mask # right shifted by 32 and masked by 16 bits
    # print('segment_1: ', segment_1)
    reverse_1 = cache_list[segment_1]
    print('reverse_1: ', reverse_1)
    # TODO working up to this point, continue for all segments, then refactor
    
    # y = reverse_0
    y = reverse_0 | reverse_1 << 16
    return y

print(reverse_bits_with_cache(x))