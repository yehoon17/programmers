from collections import deque

def restruct(n, path):
    connected = {i: [] for i in range(n)}
    for x, y in path:
        connected[x].append(y)
        connected[y].append(x)
        
    parent_of = {i: -1 for i in range(n)}
    child_of = {i: [] for i in range(n)}
    parents = deque([0])
    while parents:
        parent = parents.popleft()
        for c in connected[parent]:
            if not parent_of[parent] == c:
                child_of[parent].append(c)
                parent_of[c] = parent
                parents.append(c)
        
    return parent_of, child_of

def solution(n, path, order):
    parent_of, child_of = restruct(n, path)
    check = {y: x for x, y in order}
    
    leaves = [k for k, v in child_of.items() if not v]
    valid = {0}
    for leaf in leaves:
        visited = set()
        node = leaf
        while True:
            if node in visited:
                return False
            if node in valid:
                break
            visited.add(node)
            if node in check.keys():
                node = check[node]
            else:
                node = parent_of[node]
        valid = valid.union(visited)
    
    return True
