# First, we need to build the cache to work with. Let's examine how to reverse the bits of a 16-bit integer:
# We could use the swap_bits technique we already built, iterating i from 0 to 7 and j from 15 to 8:
# This is the same as reversing the bits of an integer. We can do this for all integers from 0 to 65535
# In the cache, the array is indexed by the integers 0 to 65535 and the values are their reversed values

# import struct

def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << i)
        x ^= bit_mask
    return x

# with open('reverse_cache', mode='wb') as reverse_cache:
reverse_list = []
# for x in range(65536):
for x in range(0, 4):
    # bitfield = [1 if digit=='1' else 0 for digit in bin(x)[2:]]
    # for x in range((8 - len(bitfield))):
    #     bitfield.insert(0, 0)
    bitfield = int('{:08b}'.format(x)[::-1], 2)
    # converts x to binary, pads with up to 8 leading zeros, the entire value is sliced in reverse order, 2 is the base passed to the int method
    print('padded bitfield: ', bitfield)

    i = 7
    j = 8
    while i >= 0:
        x = swap_bits(x, i, j)
        i = i - 1
        j = j + 1
    # print('x: ', x)
    reverse_list.append(x)


# bitlist = [x >> i & 1 for i in range(0, x.bit_length())]
# bitlist = x.to_bytes((x.bit_length() + 7) // 8, 'little')
# print('x as bitlist', int.from_bytes(bitlist, 'little'))

# x = struct.pack('>h', x)
# print('x as bitlist', x)


# with open('reverse_cache.txt', mode='w') as reverse_cache:
    # reverse_cache.write(reverse_list)
    # reverse_cache.write('\n'.join(str(word) for word in reverse_list))


# add all entries to a list
# bytes(the list)
# write the byte list to the file in one go

# WORKING FROM HERE

# ALTERNATIVE: Write as a list of integers instead?
# May be simpler
# Then export this list of integers as REVERSE_CACHE