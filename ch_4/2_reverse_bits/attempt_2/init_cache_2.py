# Take the 16 bit integers from 0 to 65535 (2^16 = 65536)
# Iterate over them, appending the reverse to a list
# Write the string representation of each element to a file
# This file is the cache. The key is the input x, and the value is its reverse

from reverse_bits_2 import reverse_bits

x = 65536
# print(reverse_bits(x, 16))

# declare the list
# for x in range
# reverse x and append it to the list
# write the string representation of each integer in the list to a 'cache' file

reverse_list = []
for x in range(8):
    reverse_list.append(reverse_bits(x, 8))

with open('reverse_cache.txt', mode='w') as reverse_cache:
    reverse_cache.write('\n'.join(str(word) for word in reverse_list))