from collections import deque


def solution(priorities, location):
    answer = 0
    deq = deque(priorities)
    priorities.sort()
    mine = deq[location]

    while True:
        temp = deq.popleft()
        location -= 1
        if temp < mine:
            continue
        else:
            if temp == priorities[-1]:
                answer += 1
                priorities.pop()
                if location < 0:
                    break
            else:
                deq.append(temp)
                if location < 0:
                    location += len(deq)

    return answer
