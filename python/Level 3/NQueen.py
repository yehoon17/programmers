def isValid(board, i, j, n):
    for k in range(i):
        if board[k][j]:
            return False

    for k in range(n):
        if i < k or j < k:
            break

        if board[i-k][j-k]:
            return False

    for k in range(n):
        if i < k or j + k >= n:
            break

        if board[i-k][j+k]:
            return False

    return True


def dfs(board, i, n):
    if i == n:
        return 1

    count = 0
    for j in range(n):
        if isValid(board, i, j, n):
            board[i][j] = True
            count += dfs(board, i+1, n)
            board[i][j] = False

    return count


def solution(n):
    answer = 0
    board = [[False for _ in range(n)] for _ in range(n)]
    return dfs(board, 0, n)
