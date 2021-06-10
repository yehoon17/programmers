from collections import deque

def get_cost(n,x,fares):
    visited = [-1 for _ in range(n)]
    visited[x-1] = 0
    deq = deque([x])
    while(deq):
        p = deq.popleft()
        for a,b,fare in fares:
            temp = fare + visited[p-1]
            if a == p:
                if visited[b-1]<0:
                    deq.append(b)
                    visited[b-1] = temp
                else:
                    visited[b-1] = min(visited[b-1], temp)
            if b == p:
                if visited[a-1]<0:
                    deq.append(a)
                    visited[a-1] = temp
                else:
                    visited[a-1] = min(visited[a-1], temp) 
    return visited
    
def solution(n, s, a, b, fares):
    s_cost = get_cost(n,s,fares)
    a_cost = get_cost(n,a,fares)
    b_cost = get_cost(n,b,fares)
    
    answer = -1
    for i in range(n):
        if s_cost[i]<0 or a_cost[i]<0 or b_cost[i]<0:
            pass
        else:
            temp = s_cost[i] + a_cost[i] +b_cost[i]
            if answer<0:
                answer = temp
            else:
                answer = min(answer,temp)
    return answer
