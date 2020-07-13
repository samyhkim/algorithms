def validate_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        # increment/decrement if element is a symbol or empty space
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        # handle upper cases
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
