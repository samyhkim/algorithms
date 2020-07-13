'''
The profit is the sum of sub-profits
Each sub-profit is the diff between selling at day j and buying at day i (with j > i)

'''


def max_profit(prices):
    if not prices or len(prices) is 1:
        return 0
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit
