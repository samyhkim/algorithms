# O(n)
def insert(intervals, new_interval):
    merged = []

    for idx, interval in enumerate(intervals):
        if interval[1] < new_interval[0]:  # no overlap
            merged.append(interval)
        elif new_interval[1] < interval[0]:  # no overlap
            merged.append(new_interval)
            return merged + intervals[idx:]  # can return earlier
        else:  # overlap case
            new_interval[0] = min(new_interval[0], interval[0])
            new_interval[1] = max(new_interval[1], interval[1])
    merged.append(new_interval)

    return merged


print(insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]])
print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
      == [[1, 2], [3, 10], [12, 16]])
