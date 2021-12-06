def solution(n, results):
    win_from = {i+1: set() for i in range(n)}
    lose_to = {i+1: set() for i in range(n)}
    for winner, loser in results:
        win_from[loser].add(winner)
        visit_win = [False for _ in range(n+1)]
        bfs = {winner}
        while bfs:
            w = bfs.pop()
            if not visit_win[w]:
                visit_win[w] = True
                winners = win_from[w]
                win_from[loser] = win_from[loser].union(winners)
                bfs = bfs.union(winners)
            
        lose_to[winner].add(loser)
        visit_lose = [False for _ in range(n+1)]
        bfs = {loser}
        while bfs:
            l = bfs.pop()
            if not visit_lose[l]:
                visit_lose[l] = True
                losers = lose_to[l]
                lose_to[winner] = lose_to[winner].union(losers)
                bfs = bfs.union(losers)
    cnt = 0
    for i in range(1, 1+n):
        if len(win_from[i]) + len(lose_to[i]) == n-1:
            cnt += 1
    
    return cnt
