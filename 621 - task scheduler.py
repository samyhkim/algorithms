from heapq import heappush, heappop
from collections import Counter

'''
The main idea is to schedule the most frequest tatsks as freqeuntly as possible
Begin with scheduling the most frequent task, then cool-off for n
During that cool-off period, schedule tasks in order of frequency
If no tasks are available, be idle

https://leetcode.com/problems/task-scheduler/discuss/130786/Python-solution-with-detailed-explanation

Why is this problem greedy?

Solution seems to be really slow.
'''


# O(n), O(1) will not be more than O(26)
def least_interval(tasks, n):
    task_frequencies = Counter(tasks)
    total_intervals = 0
    priority_queue = []  # max_heap: pop task with highest interval
    # sort from least to greatest inside of the heap
    for k, v in task_frequencies.items():
        heappush(priority_queue, (-v, k))
    # run through the heap and process the sorted tasks
    while priority_queue:
        current_cooling_interval = 0
        temp_task_holder = []
        while current_cooling_interval <= n:
            total_intervals += 1  # count interval time
            if priority_queue:
                task_frequency, task_id = heappop(priority_queue)
                # check to see if it's at the end of the overall count
                # remember that it was negative at the beginning
                if task_frequency != -1:
                    temp_task_holder.append((task_frequency + 1, task_id))
            # check to see if we're out of tasks
            # this will automatically exit out of the overall tasks
            if not priority_queue and not temp_task_holder:
                break
            else:
                current_cooling_interval += 1
        # transfer back from heap to temp to know if we should continue
        # heap => if we're not out of tasks -> temp
        # temp -> because we're not out -> heap
        for item in temp_task_holder:
            heappush(priority_queue, item)
        # we only stop if we're out of tasks
        # (constantly checking the current_heap for if it's empty)
    return total_intervals


print(least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8)
