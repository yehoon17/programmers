def f(a, tree, size):
    temp = [i for i in range(size) if sum(tree[i]) == 1]
    if not temp:
        return 0

    if len(temp) == 2:
        return abs(a[temp[0]])
        
    answer = 0
    for i in temp:
        j = [j for j in range(size) if tree[i][j] == 1][0]
        a[j] += a[i]
        answer += a[i]
        a[i] = 0
        tree[i][j] = 0
        tree[j][i] = 0

    return answer+f(a, tree, size)


def solution(a, edges):
    if not sum(a) == 0:
        return -1

    size = len(a)
    tree = [[0]*size for _ in range(size)]
    for x, y in edges:
        tree[x][y] = 1
        tree[y][x] = 1

    return f(a, tree, size)
