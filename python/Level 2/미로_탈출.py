MAX_TIME = 10000000000

def trigger(x, traps, direction):
    if x in traps:
        for key in direction[x].keys():
            direction[x][key] = not direction[x][key]
            direction[key][x] = not direction[key][x]
    
def dfs(n, x, end, direction, time, traps):
    if x == end:
        return 0
    
    trigger(x, traps, direction)
            
    min_time = MAX_TIME
    for target, is_forward in direction[x].items():
        if is_forward:
            t = dfs(n, target, end, direction, time, traps) + time[x][target]
            min_time = min(min_time, t)
            
    trigger(x, traps, direction)
            
    return min_time

def restruct(n, roads):
    direction = {i:{} for i in range(1, n+1)}
    time = {i:{} for i in range(1, n+1)}
    for x, y, t in roads:
        time[x][y] = t
        time[y][x] = t
        direction[x][y] = True
        direction[y][x] = False
    
    return direction, time
        
def solution(n, start, end, roads, traps):
    traps = set(traps)
    direction, time = restruct(n, roads)
    
    return dfs(n, start, end, direction, time, traps)
