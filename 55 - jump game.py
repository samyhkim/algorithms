'''
We go backwards to check if the index element can reach nums[-1].
If it can reach it, then index + nums[index] == goal
If it can go beyond it, then index + nums[index] > goal
Both are passing conditions and we will save that index as the new goal
Goal represents that every index it checked before can make it up to this point
By that logic, goal should equal 0 by the time we finish our loop
Otherwise, the elements before the very last check could not reach this point
'''


def can_jump(nums):
    # goal saves the last good index of element that can reach nums[-1]
    goal = len(nums) - 1

    for i in reversed(range(len(nums)-1)):
        # save index if our jump can go to goal or further
        if i + nums[i] >= goal:
            goal = i

    return goal == 0


print(can_jump([2, 3, 1, 1, 4]) == True)
print(can_jump([3, 2, 1, 0, 4]) == False)
