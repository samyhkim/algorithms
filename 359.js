class Logger {
  constructor() {
    this.hash = {};
  }

  shouldPrintMessage(timestamp, message) {
    if (!this.hash[message]) {
      this.hash[message] = timestamp;
      return true;
    } else {
      if (timestamp - this.hash[message] < 10) {
        return false;
      } else {
        this.hash[message] = timestamp;
        return true;
      }
    }
  }
}

logger = new Logger();
console.log(logger.shouldPrintMessage(1, "foo"));
console.log(logger.shouldPrintMessage(2, "bar"));
console.log(logger.shouldPrintMessage(5, "bar"));
console.log(logger.shouldPrintMessage(7, "foo"));
console.log(logger.shouldPrintMessage(11, "foo"));
