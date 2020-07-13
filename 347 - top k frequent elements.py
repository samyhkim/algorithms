import heapq


def topKFequent(nums, k):
    lookup = {}
    for i in nums:
        if i not in lookup:
            lookup[i] = 1
        else:
            lookup[i] += 1
    min_heap = []
    for key, value in lookup.items():
        if len(min_heap) == k:
            heapq.heappush(min_heap, (value, key))
            heapq.heappop(min_heap)
        else:
            heapq.heappush(min_heap, (value, key))
    return [key for (value, key) in min_heap]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFequent(nums, k))
