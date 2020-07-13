import random
'''
{1,2,3,3,3} with target 3, you want to select 2,3,4 with a probability of 1/3 each.

2 : It's probability of selection is 1 * (1/2) * (2/3) = 1/3
3 : It's probability of selection is (1/2) * (2/3) = 1/3
4 : It's probability of selection is just 1/3

So they are each randomly selected.
'''


class RandomIndex:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        random_index = None
        target_count = 0

        for index, num in enumerate(self.nums):
            if num == target:
                target_count += 1
                chance = random.randint(1, target_count)
                if chance == target_count:
                    random_index = index

        return random_index
