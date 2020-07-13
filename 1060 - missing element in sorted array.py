def missing_element(nums, k):
    if not nums or k == 0:
        return 0
    diff = nums[-1] - nums[0] + 1  # complete length
    missing = diff - len(nums)  # complete length - real length
    if k > missing:  # if k is larger than the number of missing words in sequence
        # (k - missing) is extension of leftover
        return nums[-1] + (k - missing)

    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        # nums[mid] - nums[left] is expected distance between mid number and left number
        # (mid - left) is the real distance between mid and left number
        missing = nums[mid] - nums[left] - (mid - left)
        if missing < k:
            left = mid
            k -= missing  # KEY: move left forward, we need to minus the missing words of this range
        else:
            right = mid
    # k should be between left and right index in the end
    return nums[left] + k


print(missing_element([4, 7, 9, 10], k=1))
