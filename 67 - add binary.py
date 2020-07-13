def add_binary(a, b):
    sum = ""
    a = list(a)
    b = list(b)
    carry = 0

    while a or b or carry:
        # convert to int
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())

        # convert back to str
        sum += str(carry % 2)  # ones digit
        carry //= 2  # tens digit, carry over

    # inserted in reverse order bc stack.pop()
    # have to reverse back
    return sum[::-1]
