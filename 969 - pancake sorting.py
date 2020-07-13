def pancakeSort(A):
    '''
    NOT FINISHED
    Starting state: A = [3, 2, 4, 1]
    After 1st flip: A = [1, 4, 2, 3]
    After 2nd flip: A = [4, 1, 2, 3]
    After 3rd flip: A = [3, 2, 1, 4]
    After 4th flip: A = [1, 2, 3, 4]
    '''
    res = []
    for x in range(len(A), 1, -1):
        i = A.index(x)
        res.extend([i + 1, x])
        A = A[:i:-1] + A[:i]
    return res


print(pancakeSort([3, 2, 4, 1]))
