# test the reverse_cache was written properly by reading from it

# with open('reverse_cache', mode='rb') as reverse_cache:
#     print(list(reverse_cache.read()))

f=open('reverse_cache')
lines=f.readlines()
print(lines[25])
print(lines[29])
f.close()