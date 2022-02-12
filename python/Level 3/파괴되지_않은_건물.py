def count(board):
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                cnt += 1
    return cnt


def solution(board, skill):
    degrees = {}

    for type_, r1, c1, r2, c2, degree in skill:
        degree *= (type_*2 - 3)
        area = (r1, c1, r2, c2)
        if area in degrees:
            degrees[area] += degree
        else:
            degrees[area] = degree

    for area, degree in degrees.items():
        (r1, c1, r2, c2) = area
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                board[i][j] += degree

    return count(board)
