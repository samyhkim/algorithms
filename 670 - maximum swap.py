def maximum_swap(num):
    A = list(str(num))
    ans = A[:]

    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            A[i], A[j] = A[j], A[i]
            if A > ans:
                ans = A[:]
            A[i], A[j] = A[j], A[i]

    return int("".join(ans))


print(maximum_swap("123"))
