from collections import deque
def solution(people, limit):
    full = 0
    boat = deque()
    people.sort(reverse = True)
    for i,p in enumerate(people):
        if p>limit//2:
            boat.append(limit-p)
        else:
            index = i
            break
    for i in range(len(people)-1,index-1,-1):
        p = people[i]
        while(boat):
            if p>boat[0]:
                boat.popleft()
                full+=1
            else:
                break
        if boat:
            boat[0] -= p
        else:
            boat.append(limit-p)
                
    return len(boat)+full
