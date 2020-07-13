def subarray_sum(nums, k):
    count = 0  # return number of ways we can make k
    sums = 0
    lookup = {0: 1}  # initialized for first occurence of (sums - k)

    for i in range(len(nums)):
        sums += nums[i]

        # subarray starting at index (sums - k) sums to k
        if sums - k in lookup:
            count += lookup[sums - k]

        # tracks how many times we have seen this sum
        if sums not in lookup:
            lookup[sums] = 1
        else:
            lookup[sums] += 1

    return count


print(subarray_sum([1, 2, 1, 3], 3))
print(subarray_sum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0))
