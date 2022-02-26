from itertools import combinations


def get_gap(wins):
    gap = 0
    for i in range(11):
        if i in wins:
            gap += 10 - i
        else:
            gap -= 10 - i
    return gap


def board_of(n, wins, info):
    board = [0] * 11
    for idx in wins:
        score = info[idx] + 1
        board[idx] += score
        n -= score

    board[-1] += n

    return board


def better(answer, board):
    for idx in range(10, -1, -1):
        if answer[idx] > board[idx]:
            return answer
        elif answer[idx] < board[idx]:
            return board


def solution(n, info):
    answer = [-1]
    max_gap = 0

    for n_wins in range(1, 12):
        for wins in combinations(range(11), n_wins):
            total = sum([info[idx] for idx in wins])
            if n_wins + total <= n:
                gap = get_gap(wins)
                board = board_of(n, wins, info)
                if gap > max_gap:
                    answer = board
                    max_gap = gap
                elif gap == max_gap and max_gap > 0:
                    answer = better(answer, board)

    return answer
