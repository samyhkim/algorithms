def my_atoi(s):
    intMax = pow(2, 31) - 1
    intMin = pow(-2, 31)
    s = s.strip()
    if not s:
        return 0
    sign = 1
    i = 0
    if s[i] == "+":
        i += 1
    elif s[i] == "-":
        sign = -1
        i += 1
    res = 0
    while i < len(s):
        if not s[i].isdigit():
            break
        res = res * 10 + ord(s[i]) - ord('0')
        if res > intMax:
            break
        i += 1
    return min(intMax, max(sign * res, intMin))
