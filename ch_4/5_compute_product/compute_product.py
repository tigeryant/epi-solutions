"""
Write a program that multiplies two nonnegative integers. The only operators you are allowed to use are:
- assignment
- the bitwise operators >>, <<, |, &, ~, ^
- equality checks and boolean combinations thereof

You may use loops and functions that you write yourself. These constraints imply, for example,
that you cannot use increment or decrement, or test if x < y.

Hint: Add using bitwise operations, multiply using shift-and-add
"""

# let's first tackle addition using bitwise operators

# we can iterate over the binary number, from the LSB to MSB
# we set the position bit in result based on the carry bit and the x and y position bits
# we then either set or unset the carry bit
# we increment position and the loop begins its next cycle of execution
# finally, outside the loop, we set the bit of result at position + 1 if we still have a carry bit left over
def add(x, y):
    # num_unsigned_bits = 64
    num_unsigned_bits = 128 
    result = 0
    carry = 0

    for position in range(num_unsigned_bits):
        # isolate the bits at position for each of x and y
        x_bit = (x >> position) & 1
        y_bit = (y >> position) & 1

        # x & y & carry -> 1, leave (set?) carry at 1
        # x & y not carry -> 0, set carry to 1

        # 1 of x or y, carry -> 0, set carry to 1
        # 1 of x or y, no carry -> 1, leave carry at 0

        # neither x nor y, carry -> 1, set carry to 0
        # neither x nor y, no carry -> 0, leave carry at 0

        if x_bit & y_bit:
            result |= (carry << position)
            carry = 1
        elif x_bit ^ y_bit:
            result |= ((not carry) << position)
        else:
            result |= (carry << position)
            carry = 0
        
    if carry:
        result |= (1 << (position + 1))
    return result

# print(add(4311016890794358489, 2604577139073052427)) # correct answer: 6915594029867410916
# print(f'result: {add(15, 15)}') 

# NOTE
# Using shift and add to multiply x by y
# Using shift and add to multiply achieves much better time complexity than the brute force approach

# To multiply x and y we initialize the result to 0 and iterate through the bits of x, adding 2^k * y to the result if the kth bit of x is 1.
# The value 2^k * y can be computed by left-shifting y by k (where k is the number of bits in x (-1), and is indexed from 0).

# initialise result to 0
# iterate over the bits of x, from LSB to MSB
# if the current bit is 1:
# result = result + 2^k * y
# else, if the current bit is 0:
# do nothing, (continue to the next iteration)

# to compute 2^k * y:
# we left shift y by k, where k is equal to x - 1 (think of k as the bits in y indexed by 0)

# WORKING ON
'''
def compute_product(x, y):
    num_of_bits = 64
    result = 0

    for i in range(num_of_bits): # find a better way of iterating over the bits of x later
        current = (x >> i) & 1
        if current:
            result = add(result, y << i)
    return result
'''

x = 23423423423
y = 9999999932948523984
# x = 5
# y = 8
# print(f'The product of {x} and {y} is: {compute_product(x, y)}')
# print(f'The correct answer for the product of {x} * {y} is: {x * y}')

# SOLUTION

def multiply(x, y):
    def inner_add(a, b):
        return a if b == 0 else add(a ^ b, (a & b) << 1)

    running_sum = 0
    while x:
        if x & 1:
            running_sum = inner_add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum

print(f'The product of {x} and {y} (using multiply) is: {multiply(x, y)}')
print(f'The correct answer for the product of {x} * {y} is: {x * y}')
