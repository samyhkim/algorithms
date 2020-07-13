import heapq


def k_closest(points, k):
    max_heap = []

    for x, y in points:
        distance = x ** 2 + y ** 2

        if len(max_heap) < k:
            heapq.heappush(max_heap, (-distance, x, y))
            # max_heap.push((distance, x, y))
       else:
            heapq.heappush(max_heap, (-distance, x, y))
            heapq.heappop(max_heap)
            # max_heap.push((-distance, x, y))
            # max_heap.pop()

    return [[x, y] for (distance, x, y) in max_heap]


points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(k_closest(points, k) == [[-2, 4], [3, 3]])
