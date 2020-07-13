'''
First turn the input into a set of numbers.
That takes O(n) and then we can ask in O(1) whether we have a certain number.

Then go through the numbers. If the number x is the start of a streak
(i.e., x-1 is not in the set), then test y = x+1, x+2, x+3, ... and stop
at the first number y not in the set. The length of the streak is then
simply y-x and we update our global best with that. Since we check each
streak only once, this is overall O(n).
'''


def longest_consecutive(nums):
    nums = set(nums)

    longest = 0

    for num in nums:
        if num-1 not in nums:
            next = num+1
            while next in nums:
                next += 1
            longest = max(longest, next-num)

    return longest
