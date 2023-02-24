'''
Compute quotient without arithmetical operators

Given two positive integers, compute their quotient, using only the addition, subtraction and shifting operators
'''

# attempt 2

# get more work done in each iteration
# compute the largest k such that 2^k * y <= x
# subtract 2^k * y from x
# and add 2^k to the quotient.

# We could compute the largest value of 2^k * y by iterating over values of k (starting at 0 and incrementing) and
# checking each time if the result is larger than x. We want the value that is just smaller than x

def compute_quotient(x, y):
    # if y > x to begin with, return 0
    if y > x:
        return 0

    quotient = 0

    while x >= y:
        k = 0
        # compute 2^k * y by left shifting y by k
        result = y << k
        while result < x:
            k += 1
            result = y << k
            if result > x:
                k -= 1
                result = y << k
                break

        # subtract 2^k * y from x (subtract result from x)
        x -= result
        # add 2^k to the quotient
        quotient += (1 << k)

    return quotient

x = 293842837498237498238947
y = 23894293874983
# x = 2
# y = 2
print(f'The quotient when dividing {x} by {y} = {compute_quotient(x, y)}')
print(f'The correct answer is {x // y}')
