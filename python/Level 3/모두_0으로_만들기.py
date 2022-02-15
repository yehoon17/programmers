def dfs(parent, a, tree, size, visited):
    visited[parent] = True
    total = 0

    for child in tree[parent]:
        if not visited[child]:
            a[parent] += a[child]
            total += dfs(child, a, tree, size, visited)
            total += abs(a[child])
            a[child] = 0

    return total


def solution(a, edges):
    if not sum(a) == 0:
        return -1

    size = len(a)
    visited = [False]*size
    tree = {i: [] for i in range(size)}
    for x, y in edges:
        tree[x].append(y)
        tree[y].append(x)

    return dfs(0, a, tree, size, visited)
