'''
sorted, so can use binary search
We check the sorted side in each iteration.

No rotated:
1 2 3 4 5 6 7
     mid
        
left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
3 4 5 6 7 1 2
     mid
search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side

right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
6 7 1 2 3 4 5
     mid          
search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
'''


def search(nums, target):
    if not nums:
        return

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if target == nums[mid]:
            return mid

        if nums[left] <= nums[mid]:  # left rotated
            # in ascending order side
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # right rotated
            # in ascending order side
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


print(search([6, 7, 0, 1, 2], 1) == 4)
print(search([4, 5, 6, 7, 0, 1, 2], 3) == -1)
