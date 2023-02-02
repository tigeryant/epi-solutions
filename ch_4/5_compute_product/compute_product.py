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
    num_unsigned_bits = 64
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
            if carry:
                result |= (1 << position)
            else:
                result |= (0 << position)
                carry = 1
        elif x_bit ^ y_bit:
            if carry:
                result |= (0 << position)
                carry = 1
            else:
                result |= (1 << position)
        else:
            if carry:
                result |= (1 << position)
                carry = 0
            else:
                result |= (0 << position)
        
    if carry:
        result |= (1 << (position + 1))
    return result

print(add(4311016890794358489, 2604577139073052427)) # correct answer: 6915594029867410916
# print(f'result: {add(15, 15)}') 

