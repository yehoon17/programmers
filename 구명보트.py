def solution(people, limit):
    boat = []
    for p in people:
        hasPlace = False
        for i,b in enumerate(boat):
            if p<=b:
                hasPlace = True
                boat[i]-=p
                break
        if not hasPlace:
            boat.append(limit-p)
    return len(boat)
