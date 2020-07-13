'''
if num in lookup:
    lookup[num] == 0
else:
    lookup[num] = 1
'''


def intersection(nums1, nums2):
    lookup = {}
    res = []
    for i in range(len(nums1)):
        if nums1[i] not in lookup:
            lookup[nums1[i]] = 1
    for i in range(len(nums2)):
        if nums2[i] in lookup and lookup[nums[i]] > 0:
            res.append(nums2[i])
            lookup[nums[i]] = 0
    return res


def intersection(nums1, nums2):
    lookup = {}
    res = []
    for i in range(len(nums1)):
        if nums1[i] not in lookup:
            lookup[nums1[i]] = 1
    for i in range(len(nums2)):
        if nums2[i] in lookup:
            lookup[nums2[i]] = 0
    for k, v in lookup.items():
        if v == 0:
            res.append(k)
    return res
