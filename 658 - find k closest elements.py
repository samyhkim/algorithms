'''
The array is sorted so we can use binary search.
    If we want to find a number closest to x, we use binary serach.
        So the logic is similar to find the k closest nums to x.

case 1: x - A[mid] < A[mid + k] - x, need to move window go left
-------x----A[mid]-----------------A[mid + k]----------

case 2: x - A[mid] < A[mid + k] - x, need to move window go left again
-------A[mid]----x-----------------A[mid + k]----------

case 3: x - A[mid] > A[mid + k] - x, need to move window go right
-------A[mid]------------------x---A[mid + k]----------

case 4: x - A[mid] > A[mid + k] - x, need to move window go right
-------A[mid]---------------------A[mid + k]----x------

We stop when left < right, which will be the point where left
will be the starting point for construcing our results array.

Time: O(log(n-k))
Space: O(k)
'''


def find_closest_elements(arr, k, x):
    left = 0
    right = len(arr) - k  # we want the k closest elements

    while left < right:  # can't be the same bc we need to return left chunk or right chunk
        mid = left + (right - left) // 2

        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left:left + k]


print(find_closest_elements([1, 2, 3, 4, 5], 4, 3))
