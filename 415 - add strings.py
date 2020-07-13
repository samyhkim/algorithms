def add_strings(num1, num2):
    sum = ""
    num1 = list(num1)
    num2 = list(num2)
    carry = 0

    while num1 or num2 or carry:
        # convert to int
        if num1:
            carry += ord(num1.pop()) - ord('0')
        if num2:
            carry += ord(num2.pop()) - ord('0')

        # convert back to str
        sum += str(carry % 10)  # ones digit
        carry //= 10  # tens digit, carry over

    # inserted in reverse order bc stack.pop()
    # have to reverse back
    return sum[::-1]


add_strings('234', '989')
