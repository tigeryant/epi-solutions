from compute_parity import parity3

# compute and write parity cache to file
# iterate from 0 to 65535 inclusive, finding the parity of each 'word'
# write the result to a file in binary
parity_list = [parity3(x) for x in range(65536)]
parity_bytes = bytes(parity_list)
with open('parity_cache', mode='wb') as parity_cache:
    parity_cache.write(parity_bytes)