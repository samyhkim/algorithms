def exclusive_time(n, logs):
    times = [0] * n  # return list of execution times
    stack = []
    prev_time = 0  # will always allocate prev time somewhere

    for log in logs:
        id, type, time = log.split(":")
        id, time = int(id), int(time)

        if type == "start":
            # adjust time of last log encountered
            if stack:
                # can't remove until we encounter the log's end
                times[stack[-1]] += time - prev_time
            stack.append(id)  # save current log and wait for ending pair
            prev_time = time
        else:  # will always be stack's last log's end pair
            # adjust time of last log encountered
            # can remove bc we encountered the log's end
            times[stack.pop()] += time - prev_time + 1  # zero indexed
            prev_time = time + 1  # zero indexed

    return times


logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
print(exclusive_time(2, logs))
