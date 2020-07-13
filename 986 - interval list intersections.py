'''
The steps are:

if no overlap: increment the index of the lesser interval
if overlap: overlap interval = bigger start index + lower end index.
increment the index of the lesser interval
'''


def interval_intersection(A, B):
    intervals = []
    a = b = 0
    while a < len(A) and b < len(B):
        if A[a][0] <= B[b][1] and B[b][0] <= A[a][1]:
            intervals.append(
                [max(A[a][0], B[b][0]), min(A[a][1], B[b][1])])
        if A[a][1] < B[b][1]:
            a += 1
        else:
            b += 1
    return intervals


A = [[0, 2], [5, 10], [13, 23], [24, 25]]
B = [[1, 5], [8, 12], [15, 24], [25, 26]]
print(interval_intersection(A, B))
