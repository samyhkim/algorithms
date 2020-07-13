'''
Deductions:
1. Versions are SORTED from 1 to n.
2. If is_bad == True, haven't found it yet, keep going higher.
-> BINARY SEARCH

left = 1 and r = n to look more natural

Time: O(logn)
Space: O(1)
'''


def first_bad_version(n):
    left = 1
    right = n
    while left <= right:  # could come down to when left == right
        mid = left + (right - left) // 2  # prevents overflow
        # bad version is above mid
        if is_bad_version(mid) == True:
            left = mid + 1
        # bad version is below mid
        else:
            right = mid - 1
    return left
