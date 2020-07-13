def move_zeroes(nums):
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] == 0 and nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
        if nums[i] != 0:
            i += 1
        j += 1
    return nums


print(move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0])
