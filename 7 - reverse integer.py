def reverse(x):
    result = 0
    if x < 0:
        symbol = -1
        x = -x
    else:
        symbol = 1
    while x:
        result = result * 10 + x % 10
        x //= 10
    return 0 if result > pow(2, 31) else result * symbol

# Same as above, but messier.
# def reverse(x):
#     nums = []
#     res = 0
#     if x % 10 == 0:
#         x //= 10
#     if x < 0:
#         sign = -1
#         x = -x
#     else:
#         sign = 1
#     while x is not 0:
#         temp = x % 10
#         nums.append(temp)
#         x //= 10
#     int_tens = 10 ** (len(nums)-1)
#     for i in range(len(nums)):
#         res += int_tens * nums[i]
#         int_tens //= 10
#     return 0 if res > pow(2, 31) else res * sign


print(reverse(123))
print(reverse(-123))
print(reverse(120))
