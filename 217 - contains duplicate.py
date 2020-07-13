def contains_duplicate(nums):
    lookup = {}

    for i in nums:
        if i not in lookup:
            lookup[i] = 1
        else:
            return True

    return False
