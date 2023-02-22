from compute_product import add

'''
def compute_product_1(x, y):
    result = 0
    num_of_bits = 128

    for i in range(num_of_bits):
        current = 1 & (y >> i)
        if current:
            result = add(result, (x << i))
    return result

# x = 12
# y = 13
x = 4311016890794358489
y = 2604577139073052427
print(f'The product of {x} and {y} is: {compute_product_1(x, y)}')
print(x * y)
'''

# 11101111010011110011110000010101111100100000011011011011011001

def compute_product_1(x, y):
    result = 0

    for k in range(y):
        if (y>>k)==0:
            break
    print(k)
    for i in range(add(k, 1)):
        current = 1 & (y >> i)
        if current:
            result = add(result, (x << i))
    return result

# x = 12
# y = 13
x = 4311016890794358489
y = 2604577139073052427
print(f'The product of {x} and {y} is: {compute_product_1(x, y)}')
print(x * y)
