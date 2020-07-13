def maxProfit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - max_profit)
    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]) == 5)
print(maxProfit([7, 6, 4, 3, 1]) == 0)
