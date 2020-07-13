'''
sort by start times first
if one interval's end is less than other interval's start --> no overlap
[1, 3]: ___
[6, 9]:      _____
if one interval's end is greater than other interval's started --> overlap
[1, 3]: ___
[2, 6]:  _____
'''


def merge(intervals):
    merged = []
    intervals.sort(key=lambda i: i[0])  # sort by start times

    for interval in intervals:
        # add to merged if the list of merged intervals is empty
        # or if the curr interval does not overlap with the prev
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        # otherwise, there is overlap: prev end > curr start
        # merge the greater between curr's end and prev's end
        # ex: [1, 3] and [2, 6] or [1, 5] and [2, 4]
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


input = [[1, 3], [2, 6], [8, 10], [15, 18]]
output = [[1, 6], [8, 10], [15, 18]]

print(merge(input) == output)
