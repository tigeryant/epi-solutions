"""
This problem is motivated by the following scenario. Six friends have to select a designated driver using a single unbiased coin.
The process should be fair to everyone.

How would you implement a random number generator that generates a random integer i between a and b, inclusive, given a random number generator that
produces zero or one with equal probability? All values in [a, b] should be equally likely.
"""

import random

# random number generator that produces zero or one with equal probability
def zero_one_random():
    return True if random.randint(0, 1) else False

# if x is a power of 2, we could iteratively flip the coin x/2 times. Each time, we split the space in half
# and return the half that is determined by the coin toss (lower or upper half depending on 0 or 1)
# Eventually, we're only left with one number, so we return this number

# How do we deal with the case in which x is not a power of 2?

# We could have a series of rounds of coin tossing
# Each round, we iterate over the remaining 'players'
# In each iteration, we assign that player either a 0 or a 1 based on the coin toss
# If a player's coin toss returns a 0, they are eliminated.
# The player (integer) who gets the most 1's in a row (i.e is the only one left after all others have been eliminated) is selected/returned

# Really, we don't need a tally of how many 1's each player has, we just need to know who's still in the game and eventually
# return the one who hasn't been eliminated yet

# Suppose we have a list of booleans of length x where x is the upper bound, or the number of players. Each element is set to True

def rng(x):
    players = []
    for _ in range(x):
        players.append(True)
    # add a while loop that continues until a 'winner' is selected(only 1 element of the players list is equal to true)
    still_true = x
    while still_true > 1:
        for i in range(len(players)):
            if still_true == 1:
                break
            if players[i] is True:
                players[i] = zero_one_random()
                if players[i] is False:
                    still_true -= 1

    return players.index(True) + 1 # index of player that's true

x = 5
print(f'players: {rng(x)}')
