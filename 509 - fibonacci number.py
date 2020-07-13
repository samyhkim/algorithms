def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo = [0] * (n+1)
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[-1]


print(fib(5))
