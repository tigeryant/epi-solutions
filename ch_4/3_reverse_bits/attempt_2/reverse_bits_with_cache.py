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

# segment_0: 0111000010111010 # in decimal: 28858 # reversed: (rev_0): 23822
# segment_1: 1011101100000111 # in decimal: 47879 # reversed (rev_1): 57565
# segment_2: 1111011000111010 # in decimal: 63034 # reversed (rev2): 23663
# segment_3: 0111111111001101 # in decimal: 32717 # reversed (rev3): 46078

# rev0 to binary = 0101110100001110
# rev1 to binary = 1110000011011101
# rev2 to binary = 0101110001101111
# rev3 to binary = 1011001111111110

# all 64 bits reversed: 1011001111111110010111000110111111100000110111010101110100001110 # decimal: 12969905612457336078


# importing the cache
with open('reverse_cache.txt', mode='r') as reverse_cache:
    # read each line, append it to the cache_list
    cache_list = reverse_cache.readlines()

# convert cache_list to list of integers
cache_list = [int(x) for x in cache_list]

def reverse_bits_with_cache(x):
    bit_mask = 0xFFFF
    mask_size = 16

    # find the first 16 bits of x
    segment_0 = x >> 48
    reverse_0 = cache_list[segment_0]
    print('reverse_0: ', reverse_0)
    # find the second 16 bits of x

    segment_1 = (x >> 32) & bit_mask # right shifted by 32 and masked by 16 bits
    reverse_1 = cache_list[segment_1]
    print('reverse_1: ', reverse_1)

    segment_2 = (x >> 16) & bit_mask
    reverse_2 = cache_list[segment_2]
    print('reverse_2: ', reverse_2)

    segment_3 = x & bit_mask
    reverse_3 = cache_list[segment_3]
    print('reverse_3: ', reverse_3)
    
    y = reverse_0 | reverse_1 << 16 | reverse_2 << 32 | reverse_3 << 48
    print('y: ', y)

    # refactoring
    return cache_list[x >> (3 * mask_size)] | (cache_list[(x >> (2 * mask_size)) & bit_mask] << mask_size) | (cache_list[(x >> mask_size) & bit_mask] << (2 * mask_size)) | (cache_list[x & bit_mask] << (3 * mask_size))

print(reverse_bits_with_cache(x))