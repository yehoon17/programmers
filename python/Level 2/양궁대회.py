from itertools import combinations


def is_winable(n, info, overtake_idx):
    total = sum([info[i] for i in overtake_idx])
    return len(overtake_idx) + total <= n


def compare_score(info, overtake_idx):
    score_gap = 0
    for i in range(11):
        score = 10 - i
        if i in overtake_idx:
            score_gap += score
        elif info[i] > 0:
            score_gap -= score

    return score_gap


def board_of(n, overtake_idx, info):
    board = [0]*11
    for i in overtake_idx:
        score = info[i] + 1
        board[i] += score
        n -= score

    board[-1] += n

    return board


def better(best_board, board):
    for idx in range(10, -1, -1):
        if best_board[idx] > board[idx]:
            return best_board
        elif best_board[idx] < board[idx]:
            return board


def solution(n, info):
    best_board = [-1]
    max_score_gap = 0

    for n_wins in range(1, 10):
        for overtake_idx in combinations(range(11), n_wins):
            if is_winable(n, info, overtake_idx):
                score_gap = compare_score(info, overtake_idx)
                board = board_of(n, overtake_idx, info)
                if score_gap > max_score_gap:
                    best_board = board
                    max_score_gap = score_gap
                elif score_gap == max_score_gap and max_score_gap > 0:
                    best_board = better(best_board, board)

    return best_board
