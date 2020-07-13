def divide(dividend, divisor):
    max_int = pow(2, 31) - 1
    min_int = pow(-2, 31)
    sign = 1
    if dividend == 0 or divisor == 0:
        return 0
    elif dividend < 0 < divisor or divisor < 0 < dividend:
        sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
    else:  # both negative or both positive
        dividend = abs(dividend)
        divisor = abs(divisor)
    res = 0
    while dividend >= divisor:
        temp, val = divisor, 1
        while dividend >= temp + temp:
            temp += temp
            val += val
        res += val
        dividend -= temp
    if sign == 1:
        return min(max_int, res)
    else:
        return max(min_int, 0-res)


dividend = 10
divisor = -3
print(divide(dividend, divisor))
