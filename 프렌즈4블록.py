from itertools import product

class Board:
    def __init__(self, m, n, board):
        self.height = m
        self.width = n
        self.board = [[x for x in line] for line in board]
    
    def play(self):
        cnt = 0
        while True:
            heads = self.heads()
            if not heads:
                break
            cnt += self.remove(heads)
            self.fill_down()
        return cnt
    
    def heads(self):
        heads = []
        for i in range(self.height-1):
            for j in range(self.width-1):
                if self.is_head(i, j):
                    heads.append((i, j))
        return heads
    
    def is_head(self, i, j):
        if self.board[i][j]:
            area = product(range(2), range(2))
            if len({self.board[i+x][j+y] for x, y in area}) == 1:
                return True
        return False
                
    def remove(self, heads):
        cnt = 0
        for i, j in heads:
            area = product(range(2), range(2))
            for x, y in area:
                if self.board[i+x][j+y]:
                    self.board[i+x][j+y] = None
                    cnt += 1
        return cnt
        
    def fill_down(self):
        for j in range(self.width):
            for i in range(self.height-1, 0, -1):
                if not self.board[i][j]:
                    z = 1
                    while i-z >= 0:
                        if self.board[i-z][j]:
                            self.board[i][j] = self.board[i-z][j]
                            self.board[i-z][j] = None
                            break
                        z += 1
    
    
def solution(m, n, board):
    b = Board(m, n, board)
    return b.play()
