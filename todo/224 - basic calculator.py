def calculate(s):
    res = 0
    num = 0
    sign = 1
    stack = []
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        elif s[i] in '+-':
            res += sign * num
            num = 0
            if s[i] == '+':
                sign = 1
            else:
                sign = -1
        elif s[i] == '(':
            stack.append(res)
            stack.append(sign)
            sign = 1
            res = 0
        elif s[i] == ')':
            res += sign * num
            res *= stack.pop()
            res += stack.pop()
            num = 0
    return res + num * sign


print(calculate("(7+(4+5+2)-3)"))
