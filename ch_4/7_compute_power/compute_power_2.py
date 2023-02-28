"""
Write a program that takes a double x and an integer y and returns x^y. You can ignore overflow and underflow.
"""

# attempt 2

def compute_power(x: float, y: int) -> float:
    # multiply x by 10 until it's an integer. record the number of times you had to do this
    # find the sum of all the new x left shifted by the various parts of y, where the parts of y are just it's constituent powers of 2
    # In binary, we can see what y is composed of by seeing which of its bits are set.
    # Once we've calculated this cumulative total, we can divide it by 10 the same number of times we multiplied it by 10 earlier
    # We return this result

    # At the end of each iteration, we can right shift x by one. Eventually x == 0 and the loop breaks

    # define x_int as x multiplied by 10 enough times to make it an integer
    x_int = x # temporary

    running_sum = 1
    position = 0
    while y:
        print(f'y = {y}')
        if y & 1:
            print(f'triggered')
            print(f'x_int << position = {x_int << position}')
            # bug is on the line below this
            running_sum = running_sum * (x_int << position) # x_int leftshifted by (1 left shifted by the the number of iterations that this loop has been through, some counter)
            print(f'running sum = {running_sum}')
            # consider this counter the position of the current bit
        position += 1
        y >>= 1
    
    return running_sum

    # divide x_int by 10 the same amount of times as it was multiplied by before
    # return this

x = 2
y = 4
print(f'{x} raised to the power of {y} = {compute_power(x, y)}')
print(f'The correct answer is: {pow(x, y)}')