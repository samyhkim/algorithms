def check_subarray_sum(nums, k):
    lookup = {0: -1}
    sum = 0

    for i, n in enumerate(nums):
        if k != 0:
            sum = (sum + n) % k
        else:
            sum += n

        if sum not in lookup:
            lookup[sum] = i
        else:
            if i - lookup[sum] >= 2:
                return True

    return False
