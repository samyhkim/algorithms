def calculate(s):
    if len(s) == 0:
        return
    stack = []
    num = 0
    sign = '+'  # kickstarter to allow first case, assuming all ints in s are positive
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])

        # last element is an int but we need to add to stack
        if s[i] in '+-*/' or i == len(s)-1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
            num = 0
            sign = s[i]
    return sum(stack)
