import heapq


# O(k+(n-k)lgk) time, min-heap
def find_kth_largest(nums, k):
    min_heap = []
    for i in nums:
        heapq.heappush(min_heap, i)
    for i in range(len(nums) - k):
        heapq.heappop(min_heap)
    return heapq.heappop(min_heap)


# O(n) time, quick selection
def findKthLargest(self, nums, k):
    # convert the kth largest to smallest
    return self.findKthSmallest(nums, len(nums)+1-k)


def findKthSmallest(self, nums, k):
    if nums:
        pos = self.partition(nums, 0, len(nums)-1)
        if k > pos+1:
            return self.findKthSmallest(nums[pos+1:], k-pos-1)
        elif k < pos+1:
            return self.findKthSmallest(nums[:pos], k)
        else:
            return nums[pos]


# choose the right-most element as pivot
def partition(self, nums, l, r):
    low = l
    while l < r:
        if nums[l] < nums[r]:
            nums[l], nums[low] = nums[low], nums[l]
            low += 1
        l += 1
    nums[low], nums[r] = nums[r], nums[low]
    return low
