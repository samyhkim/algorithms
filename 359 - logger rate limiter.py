class Logger:

    def __init__(self):
        self.hash = {}

    def should_print_message(self, timestamp, message):
        if message not in self.hash:
            self.hash[message] = timestamp
            return True
        else:
            if timestamp - self.hash[message] < 10:
                return False
            else:
                self.hash[message] = timestamp
                return True
