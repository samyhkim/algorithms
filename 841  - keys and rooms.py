def can_visit_all_rooms(rooms):
    return len(dfs(rooms, [], 0)) == len(rooms)


def dfs(rooms, visited_rooms, curr_room):
    visited_rooms += [curr_room]

    for key in rooms[curr_room]:
        # haven't seen key before, key represents next room
        # enter room to see what keys the next room has
        if key not in set(visited_rooms):
            dfs(rooms, visited_rooms, key)

    return visited_rooms


print(can_visit_all_rooms([[1, 3], [3, 0, 1], [2], [0]]))
print(can_visit_all_rooms([[1], [2], [3], []]))
