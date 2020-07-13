def canAttendMeetings(intervals):
    '''
    sort by start times first
    if there is any overlap, return False
    if current interval's start is less than last interval's end --> overlap
    '''
    intervals.sort(key=lambda i: i[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][-1]:
            return False
    return True


input1 = [[0, 30], [5, 10], [15, 20]]
input2 = [[7, 10], [2, 4]]

print(canAttendMeetings(input1) == False)
print(canAttendMeetings(input2) == True)
