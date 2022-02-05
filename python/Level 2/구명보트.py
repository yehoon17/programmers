from collections import deque


def solution(people, limit):
    full = 0
    boat = deque()
    people.sort(reverse=True)

    for i, p in enumerate(people):
        if p > limit//2:
            boat.append(limit-p)
        else:
            for j in range(len(people)-1, i-1, -1):
                p = people[j]
                while boat:
                    if p > boat[0]:
                        boat.popleft()
                        full += 1
                    else:
                        break
                if boat:
                    boat[0] -= p
                else:
                    boat.append(limit-p)
            break

    return len(boat) + full
