def two_sum(nums, target):
    lookup = {}

    for i in range(len(nums)):
        difference = target - nums[i]

        if difference not in lookup:
            lookup[nums[i]] = i
            print(lookup)
        else:
            return [i, lookup[difference]]


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
