from collections import Counter
import heapq


def reorganize_string(S):
    reorganized_string = ""
    c = Counter(S)

    # use Counter instead of manual dictionary bc
    # can't put value in key's position
    max_heap = [(-value, key) for key, value in c.items()]
    heapq.heapify(max_heap)
    prev_freq = 0
    prev_char = ""

    while max_heap:
        freq, char = heapq.heappop(max_heap)
        reorganized_string += char
        freq += 1

        # reinsert back into heap if char's freq < 0
        if prev_freq < 0:
            heapq.heappush(max_heap, (prev_freq, prev_char))
        prev_freq = freq
        prev_char = char

    # if reorganized string and original are not the same, invalid
    if len(reorganized_string) != len(S):
        return ""
    else:
        return reorganized_string


print(reorganize_string('aab'))
