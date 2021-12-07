def move(bfs, maps, n_row, n_col):
    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    new_bfs = set()
    for x, y in bfs:
        maps[x][y] = 0
        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy    
            if -1 < new_x < n_row and -1 < new_y < n_col:
                if maps[new_x][new_y] == 1:
                    new_bfs.add((new_x, new_y))
    
    return new_bfs
    
def solution(maps):
    n_row = len(maps)
    n_col = len(maps[0])
    
    answer = 1
    bfs = {(0, 0)}
    while bfs:
        if (n_row-1, n_col-1) in bfs:
            return answer
        bfs = move(bfs, maps, n_row, n_col)
        answer += 1
    
    return -1
