def find_diagonal_order(mat):
    if not mat:
        return
    diagonal_order = []
    lookup = {}

    # Step 1: Numbers are grouped by the diagonals.
    # Numbers in same diagonal have same value of row+col
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i + j in lookup:
                lookup[i + j].append(mat[i][j])
            else:
                lookup[i + j] = [mat[i][j]]

    # Step 2: Place diagonals in the result list.
    # But remember to reverse numbers in even keys
    for key in sorted(lookup.keys()):
        if key % 2 == 0:
            lookup[key].reverse()

        # append(lookup[key]) returns [[1], [2, 4], [7, 5, 3], [6, 8], [9]]
        diagonal_order += lookup[key]

    return diagonal_order


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(find_diagonal_order(matrix))
