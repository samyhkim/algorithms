class MovingAverage {
  constructor(size) {
    this.queue = [];
    this.queue_size = 0;
    this.max_size = size;
    this.sum = 0;
  }

  next(val) {
    this.queue.push(val);
    this.sum += val;

    if (this.size === this.max_size) {
      this.sum -= this.queue.shift();
    } else {
      this.queue_size += 1;
    }

    return this.sum / this.queue_size;
  }
}

movingAverage = new MovingAverage(3);
console.log(movingAverage.next(1));
console.log(movingAverage.next(3));
console.log(movingAverage.next(10));
console.log(movingAverage.next(5));
