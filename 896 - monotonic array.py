def is_monotonic(A):
    if len(A) <= 2:
        return True

    is_increasing = False
    is_decreasing = False
    for i in range(1, len(A)):
        if A[i - 1] > A[i]:
            is_increasing = True
        elif A[i - 1] < A[i]:
            is_decreasing = True

        if is_increasing and is_decreasing:
            return False

    return True
