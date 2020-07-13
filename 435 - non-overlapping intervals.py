def eraseOverlapIntervals(intervals):
    '''
    sort by end times
    if curr start > last end --> overlap:
        update end to curr end
    else --> no overlap:
        count += 1
    '''
    end = float('-inf')
    erased = 0
    intervals.sort(key=lambda i: i[1])
    for i in range(len(intervals)):
        if intervals[i][0] >= end:
            end = intervals[i][1]
        else:  # start is less than end --> overlap
            erased += 1
    return erased


input1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
input2 = [[1, 2], [1, 2], [1, 2]]
input3 = [[1, 2], [2, 3]]

print(eraseOverlapIntervals(input1) == 1)
print(eraseOverlapIntervals(input2) == 2)
print(eraseOverlapIntervals(input3) == 0)
