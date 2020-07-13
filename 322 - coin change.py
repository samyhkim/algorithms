def coinChange(coins, target):
    memo = [float('inf')] * (target+1)
    memo[0] = 0
    for i in range(1, target+1):
        for coin in coins:
            if i-coin >= 0:
                memo[i] = min(memo[i], 1 + memo[i-coin])
    if memo[-1] == float('inf'):
        return -1
    return memo[-1]


print(coinChange([1, 2, 5], 11))
