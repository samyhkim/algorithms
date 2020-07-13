import heapq


def last_stone_weight(stones):
    stones = [-val for val in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        x1 = heapq.heappop(stones)
        x2 = heapq.heappop(stones)
        if x1 != x2:
            heapq.heappush(stones, -abs(x1 - x2))
    if len(stones) == 0:
        return 0
    return -stones[0]


print(last_stone_weight([2, 7, 4, 1, 8, 1]))
