def valid_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            one = s[left:right]  # raceckar: cec == cec
            two = s[left + 1:right + 1]  # raceckar: eck != kce
            # check windows excluding each offending letter
            # if either returns True, we can have a palindrome
            return one == one[::-1] or two == two[::-1]

        left += 1
        right -= 1

    return True


print(valid_palindrome('aba'))
print(valid_palindrome('aabcdaa'))
