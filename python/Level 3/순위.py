def cascade(player, result_of, n):
    visited = [False for _ in range(n+1)]
    players = []
    bfs = {player}

    while bfs:
        p = bfs.pop()
        if not visited[p]:
            visited[p] = True
            players.append(p)
            bfs = bfs.union(result_of[p])

    return players


def solution(n, results):
    win_from = {i+1: set() for i in range(n)}
    lose_to = {i+1: set() for i in range(n)}
    
    for winner, loser in results:
        winners = cascade(winner, win_from, n)
        losers = cascade(loser, lose_to, n)
        for w in winners:
            for l in losers:
                win_from[l].add(w)
                lose_to[w].add(l)

    cnt = 0
    for i in range(1, 1+n):
        if len(win_from[i]) + len(lose_to[i]) == n-1:
            cnt += 1

    return cnt
