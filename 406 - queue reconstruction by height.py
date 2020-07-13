def reconstruct_queue(people):
    people.sort(key=lambda x: (-x[0], x[1]))
    queue = []
    for p in people:
        queue.insert(p[1], p)
    return queue


input = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
output = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
print(reconstruct_queue(input) == output)
