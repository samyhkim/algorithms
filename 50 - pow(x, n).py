def pow(x, n):
    if n == 0:
        return 1
    if n == -1:
        return 1 / x
    if x == 0:
        return 0
    elif n % 2 == 0:
        result = pow(x, n // 2)
        return result * result
    else:
        return x * pow(x, n - 1)


# Iterative - O(n)
def pow(x, n):
    result = 1
    for i in range(abs(n)):
        if n < 0:
            result *= 1 / x
        else:
            result *= x
    return result
