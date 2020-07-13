'''
Basic idea:
1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
    so we only have to care about those elements in this range and remove the rest.
2. we can use the array index as the hash to restore the frequency of each number within
        the range [1,...,l+1]
'''


def first_missing_positive(nums):
    for i in range(len(nums)):
        first = nums[i]-1
        second = nums[nums[i]-1]
        while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
            tmp = nums[i]-1
            nums[i], nums[tmp] = nums[tmp], nums[i]
    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    return len(nums)+1


print(first_missing_positive([1, 2, 0]) == 3)
print(first_missing_positive([3, 4, -1, 1]) == 2)
print(first_missing_positive([7, 8, 9, 11, 12]) == 1)
