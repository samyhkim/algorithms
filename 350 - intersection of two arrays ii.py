def intersect(nums1, nums2):
    counts = {}
    res = []
    for num in nums1:
        counts[num] = counts.get(num, 0) + 1
    for num in nums2:
        if num in counts and counts[num] > 0:
            res.append(num)
            counts[num] -= 1
    return res


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 5, 4]
print(intersect(nums1, nums2))
