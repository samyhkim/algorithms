def merge(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        elif nums1[m - 1] <= nums2[n - 1]:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1

    nums1[:n] = nums2[:n]  # special case when num1 is none


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
