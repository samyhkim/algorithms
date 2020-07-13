def walls_and_gates(rooms):
    if len(rooms) == 0 or len(rooms[0]).length == 0:
        return

    queue = []

    for row in range(len(rooms)):
        for col in range(len(rooms[0])):
            if rooms[row][col] == 0:
                queue.append([row, col])

    while queue:
        row, col = queue.pop(0)
        for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0 <= row + i < len(rooms) and 0 <= col + j < len(rooms[0]):
                if rooms[row + i][col + j] == 2147483647:
                    rooms[row + i][col + j] = rooms[row][col] + 1
                    queue.append([row+i, col + j])
