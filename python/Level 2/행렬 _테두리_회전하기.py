def solution(rows, columns, queries):
    answer = []
    board = [[i + j*columns + 1 for i in range(columns)] for j in range(rows)]

    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        temp = board[x1][y1]
        m = temp
        for i in range(x1, x2):
            board[i][y1] = board[i+1][y1]
            if m > board[i][y1]:
                m = board[i][y1]

        for i in range(y1, y2):
            board[x2][i] = board[x2][i+1]
            if m > board[x2][i]:
                m = board[x2][i]

        for i in range(x2, x1, -1):
            board[i][y2] = board[i-1][y2]
            if m > board[i][y2]:
                m = board[i][y2]

        for i in range(y2, y1+1, -1):
            board[x1][i] = board[x1][i-1]
            if m > board[x1][i]:
                m = board[x1][i]

        board[x1][y1+1] = temp
        answer.append(m)

    return answer
