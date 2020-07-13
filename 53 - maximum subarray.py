'''
if we encounter a negative index element
    if i element turns running_sum negative
        continue
    else
        nums[i] += nums[i-1]
return max(nums)
'''


def max_subarray(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)


input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output = 6

print(max_subarray(input) == output)
