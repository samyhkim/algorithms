# Solved using O(n) space, FIX TO O(1) SPACE

# Note: should run in O(n) time with O(1) space


def firstMissingPositive(nums):
    # if len(nums) == 0:
    #     return 1
    # lookup = {}
    # for i in range(len(nums)):
    #     if nums[i] not in lookup:
    #         lookup[nums[i]] = nums[i]
    # first_positive = 1
    # while first_positive in lookup:
    #     first_positive += 1
    # return first_positive
    for i in range(len(nums)):
        while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
            tmp = nums[i]-1
            nums[i], nums[tmp] = nums[tmp], nums[i]
    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    return len(nums)+1


print(firstMissingPositive([1, 2, 0, 4]) == 3)
print(firstMissingPositive([3, 4, -1, 1]) == 2)
print(firstMissingPositive([12, 7, 8, 9, 11]) == 1)
print(firstMissingPositive([-12, -7, -8, -9, -11]) == 1)
print(firstMissingPositive([]) == 1)
print(firstMissingPositive([0]) == 1)
print(firstMissingPositive([-1]) == 1)
print(firstMissingPositive([1, 1, 1]) == 2)


'''
duplicates?

if nums is empty
    return 1

add nums to lookup - O(n)
first_positive = 1
while first_positive in lookup:
    first_positive += 1
return first_positive





if 1 is found
saved += 1
saved = 1
for i in range(len(nums)):
    if nums[i] < saved:
        saved = nums[i]
    
return saved
1 < 2
saved = 1 + 1
look for saved in nums:
    if saved is found:
        saved += 1
if nums[i] < saved:
    saved = nums[i]
'''
