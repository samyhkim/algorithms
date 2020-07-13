def find_judge(N, trust):
    # N is vertices, pairs in trust are edges, trust is the graph
    count = [0] * (N + 1)  # compensate for zero-indexed arrays

    # count all the in-degrees
    for i, j in trust:
        count[i] -= 1
        count[j] += 1

    # there are N vertices, and if there is a single
    # vertice with all the in-degrees, then that vertice
    # should have a count of N - 1, which represents the
    # subtraction of itself
    for i in range(N): # compensate for zero-indexed arrays
        if count[i] == N - 1:
            return i

    return - 1


print(find_judge(3, [(1, 3), (2, 3)]))
