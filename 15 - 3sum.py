'''
Why does i check backwards but j checks forwards?
If i is the same as before, then we have checked every combination already.
We always start j from i + 1 bc every combination from 0~i has been tried.
'''


def three_sum(nums):
    nums.sort()  # pre-processing

    triplets = []

    for i in range(len(nums) - 2):
        # start left-most pointer from i+1 bc combinations 0~i have been tried
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]

            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            elif sum == 0:
                triplets.append([nums[i], nums[left], nums[right]])

                # move pointers to the next diff numbers to avoid repeats
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # NEED TO INCREMENT ONE MORE TIME BC WHILE CHECKS STOP BEFORE
                left += 1
                right -= 1

    return triplets


print(three_sum([-1, 0, 1, 2, -1, -4]))

# O(nlogn) + O(n^2) = O(n^2)
