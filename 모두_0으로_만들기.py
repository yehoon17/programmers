from collections import deque

def solution(a, edges):
    if not sum(a) == 0:
        return -1
    
    answer = 0
    size = len(a)
    tree = [[0 for _ in range(size)] for _ in range(size)]
    for x,y in edges:
        tree[x][y] = 1
        tree[y][x] = 1
    
    bfs = deque([i for i in range(size) if sum(tree[i]) == 1])
    visited=[False for _ in range(size)]
    
    while(bfs):
        i = bfs.popleft()
        visited[i]=True
        temp = [j for j in range(size) if tree[i][j]==1]
        j=-1
        for x in temp:
            if not visited[x]:
                j = x
                break
        if j<0:
            break
        a[j]+=a[i]
        answer+=a[i]
        temp=[]
        for k in range(size):
            if tree[j][k] == 1:
                if not visited[k]:
                    temp.append(k)
        if len(temp) == 1:
            bfs.append(temp[0])
    
    return answer
