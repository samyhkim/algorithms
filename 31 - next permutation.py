'''
Best approach to generate all permutations is to start at the lowest
permutation, and repeatedly compute the next permutation in place.

Key observation: when we want to compute the next permutation, we must
"increase" the sequence as little as possible.

1. Identify the longest suffix that is non-increasing.
    Find largest index i such that nums[i-1] < nums[i]
    (if no such i exists, then this is already the last permutation)
2. Look at the element immediately to the left of the suffix, the pivot.
    Find largest index j such that j >= i and nums[j] > nums[i-1]
3. Swap the pivot with the smallest element in the suffix greater than the pivot.
    Swap nums[j] and nums[i-1]
4. Finally, reverse the suffix, bc the replaced element respects the decreasing order.
    Reverse the suffix starting at nums[i]
'''


def next_permutation(nums):
    i = len(nums) - 1
    # decrease i until suffix is non-increasing
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1

    # if greatest number is nums[0], then nums are in descending order
    if i == 0:
        return nums.reverse()

    # find next greater element than pivot in suffix, then swap
    pivot = i - 1  # last "ascending" position; the pivot
    j = len(nums) - 1  # next greater element than pivot in suffix
    while nums[j] <= nums[pivot]:
        j -= 1
    nums[pivot], nums[j] = nums[j], nums[pivot]

    # reverse suffix
    left = pivot + 1  # start of suffix
    right = len(nums) - 1  # end of suffix
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


print(next_permutation([1, 2, 3]))
print(next_permutation([3, 2, 1]))
print(next_permutation([1, 1, 5]))
