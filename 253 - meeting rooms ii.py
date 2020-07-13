'''
get interval start times
get interval end times
only need to check all start times --> start time overlaps us total overlaps
if current interval's start is less than last interval's end --> overlap
if overlap:
    num_rooms += 1
else:
    get next end interval
'''


def minMeetingRooms(intervals):
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)
    num_rooms = 0
    e = 0
    for s in range(len(starts)):
        start_interval = starts[s]
        end_interval = ends[e]
        if start_interval < end_interval:
            num_rooms += 1
        else:
            e += 1
    return num_rooms


input1 = [[0, 30], [5, 10], [15, 20]]
input2 = [[7, 10], [2, 4]]

print(minMeetingRooms(input1) == 2)
print(minMeetingRooms(input2) == 1)
