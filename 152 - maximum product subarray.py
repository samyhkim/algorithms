'''
You have 3 choices at any position in the array:
1. You can get the max prod by multiplying the curr elem w max prod
calculated so far (might work when curr elem is positive)

2. You can get the max prod by multiplying the curr elem w min prod
calculated so far (might work when curr elem is negative)

3. Curr elem might be a starting position for max prod subarray
'''


def max_product(nums):
    global_max = nums[0]
    local_max = nums[0]
    local_min = nums[0]

    for i in range(1, len(nums)):
        temp = local_max  # holds local max/min before value is changed
        local_max = max(nums[i], nums[i] * local_max, nums[i] * local_min)
        local_min = min(nums[i], nums[i] * temp, nums[i] * local_min)

        global_max = max(global_max, local_max)

    return global_max


print(max_product([2, -3, 4, -8, 0]))
