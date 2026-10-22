import heapq


def can_attend_all(events):
    events = sorted(events)

    for i in range(1, len(events)):
        # start == previous end is okay
        if events[i][0] < events[i - 1][1]:
            return False

    return True


def min_rooms_required(events):
    if not events:
        return 0

    events = sorted(events)
    rooms = []  # min-heap: end time of the last event in each room

    for start, end in events:
        # reuse a room if its previous event has finished
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)

        heapq.heappush(rooms, end)

    return len(rooms)


tests = [
    [],                                  # True, 0
    [(9, 10), (10, 11), (11, 12)],       # True, 1
    [(9, 12), (10, 11)],                 # False, 2
    [(1, 5), (2, 6), (3, 7), (8, 9)],    # False, 3
    [(10, 11), (9, 10)],                 # True, 1
    [(1, 10), (2, 3), (4, 5), (6, 7)],   # False, 2
    [(9, 10), (9, 10), (9, 10)]          # False, 3
]

for events in tests:
    print(events, can_attend_all(events), min_rooms_required(events))
