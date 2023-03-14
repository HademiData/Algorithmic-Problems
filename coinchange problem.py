'''
Coin Change Problem
Suppose you have a set of coins with different denominations and you want to make a certain 
amount of change using the minimum number of coins possible. A greedy algorithm for this problem would work as follows:

Sort the coins in descending order based on their denominations.
Starting with the largest denomination coin, continue adding coins to the solution until the desired amount of change is reached.
'''

def coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

coins = [25, 10, 5, 1]
amount = 63
print(coin_change(coins, amount))
# Output: [25, 25, 10, 1, 1, 1]


'''
In the above code, we sort the coins in descending order and then loop through 
them. We add the largest denomination coin possible at each step until we reach 
the desired amount of change. The resulting list of coins represents the minimum number of coins required to make the desired amount of change.
'''
