'''
Moving Average m = new Moving Average(3)
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''


class MovingAverage:

    def __init__(self, size):
        self.queue = []
        self.queue_size = 0
        self.max_size = size
        self.sum = 0

    def next(self, val):
        self.queue.append(val)
        self.sum += val

        if self.queue_size == self.max_size:
            self.sum -= self.queue.pop(0)
        else:
            self.queue_size += 1

        return self.sum / self.queue_size


'''
Variablizing queue_size is better than calling len(queue) every time:
1. Clear name
2. Clear suggestion of its use
3. Takes away the need to call len(queue) function every time
4. Allows to call queue_size attribute elsewhere in class, if necessary
'''
