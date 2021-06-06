from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    time = 0
    total_weight = 0
    bridge = deque([0]*bridge_length)
    
    while(True):
        total_weight-=bridge.popleft()
        bridge.append(0)
        if trucks:
            if total_weight + trucks[0] <= weight:
                bridge[-1] = trucks[0]
                total_weight += trucks.popleft()
        time += 1
        if total_weight == 0:
            break
            
    return time
