x = 8123010520786304973 

# importing the cache and assign it to a list
with open('reverse_cache.txt', mode='r') as reverse_cache:
    cache_list = reverse_cache.readlines()

# convert cache_list to list of integers
cache_list = [int(x) for x in cache_list]

# reverse bits by reference to the pre-computed cache
def reverse_bits_with_cache(x):
    bit_mask = 0xFFFF
    mask_size = 16
    return cache_list[x >> (3 * mask_size)] | (cache_list[(x >> (2 * mask_size)) & bit_mask] << mask_size) | (cache_list[(x >> mask_size) & bit_mask] << (2 * mask_size)) | (cache_list[x & bit_mask] << (3 * mask_size))

print(reverse_bits_with_cache(x))
