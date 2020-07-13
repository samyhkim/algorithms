def rob(homes):
    if not homes:
        return 0
    memo = [0] * len(homes)
    memo[0] = homes[0]
    memo[1] = max(homes[0], homes[1])
    for i in range(2, len(homes)):
        memo[i] = max(memo[i-1], memo[i-2] + homes[i])
    return memo[-1]


print(rob([2, 7, 9, 3, 1]))
