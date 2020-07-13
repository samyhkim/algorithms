# version 1
def longest_palindrome(s):
    max_palindrome = ""

    for i in range(len(s)):
        # type_1: isolated palindrome element "aba"
        type_1 = palindrome_counter(s, i, i)
        if len(type_1) > len(max_palindrome):
            max_palindrome = type_1

        # type_2: adjacent palindrome elements "abba"
        type_2 = palindrome_counter(s, i, i + 1)
        if len(type_2) > len(max_palindrome):
            max_palindrome = type_2

    return max_palindrome


# get longest palidrome possible from inner to outer
# l, r are the middle indexes
def palindrome_counter(s, left, right):
    while 0 <= left and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return s[left+1:right]


# version 2
# def longest_palindrome(s):
#     res = ""
#     for i in range(len(s)):
#         # 0: odd case "aba", 1: even case "abba"
#         for k in range(2):
#             temp = helper(s, i, i + k)
#             # found new longest
#             if len(temp) > len(res):
#                 res = temp
#     return res


print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
