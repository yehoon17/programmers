def winners_of(winner, win_from, n):
    visited = [False for _ in range(n+1)]
    winners = []
    bfs = {winner}
    while bfs:
        w = bfs.pop()
        if not visited[w]:
            visited[w] = True
            winners.append(w)
            bfs = bfs.union(win_from[w])

    return winners

def losers_of(loser, lose_to, n):
    visited = [False for _ in range(n+1)]
    losers = []
    bfs = {loser}
    while bfs:
        l = bfs.pop()
        if not visited[l]:
            visited[l] = True
            losers.append(l)
            bfs = bfs.union(lose_to[l])

    return losers
    
def solution(n, results):
    win_from = {i+1: set() for i in range(n)}
    lose_to = {i+1: set() for i in range(n)}
    for winner, loser in results:
        winners = winners_of(winner, win_from, n)
        losers = losers_of(loser, lose_to, n)
        for w in winners:
            for l in losers:
                win_from[l].add(w)
                lose_to[w].add(l)
        
    cnt = 0
    for i in range(1, 1+n):
        if len(win_from[i]) + len(lose_to[i]) == n-1:
            cnt += 1
    
    return cnt
