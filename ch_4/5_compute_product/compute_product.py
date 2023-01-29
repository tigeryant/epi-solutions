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
# two set bits in the same position add to make a set bit to their left
# a set and unset bit, produces a set bit
# no set bits produce no set bit

# we could iterate over the words, starting with the MSBs (where position is at its maximum)
# on each iteration, we evaluate compare the bits in that position
# suppose that position is indexed from 0, starting with the LSB
# if both bits are set, we set the bit at position + 1 in the result (AND)
# if one bit is set, we set the bit at position in the result (XOR)
# else, if neither, we don't set any bit

# let's assume that we are working with 64 bit integers

def add(x, y):
    num_unsigned_bits = 4
    result = 0
    for i in range(4):
        position = num_unsigned_bits - i - 1
        # position = num_unsigned_bits - i + 1
        # print(f'i: {i}, position: {position}')

        # isolate the bits at position for each of x and y
        x_bit = (x >> position) & 1
        print(f'x_bit: {x_bit}')
        y_bit = (y >> position) & 1
        print(f'y_bit: {y_bit}')
        
        # error should be here somewhere
        if x_bit & y_bit:
            # TODO bug is here -> if we set the bit to the left in result, but that bit is already set, this operation has no effect
            # we need to rewrite this logic to account for this
            # if we set a bit to the left but it's already set, we need to handle this
            result |= (1 << (position + 1))
            print(f'AND at position {position}, result: {result}')
        elif x_bit ^ y_bit:
            result |= (1 << position)
            print(f'XOR at position {position}, result: {result}')
    return result

# 8421  8421
# 0100, 1100

# 4 + 12 is 16, which is 10000
# TODO consider scrapping and re-writing, as this is flawed. Or see solution

# print(add(97, 2))
# print(add(4311016890794358489, 2604577139073052427)) # correct answer: 6915594029867410916
# print(add(5, 15))
# TODO debug - why is this 10? work through the logic on paper
print(add(4, 12)) # 0100, 1100