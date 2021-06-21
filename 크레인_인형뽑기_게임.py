def solution(board, moves):
    answer=0
    size = len(board)
    dolls = [[] for _ in range(size)]
    for i in range(size-1,-1,-1):
        for j in range(size):
            if board[i][j] > 0:
                dolls[j].append(board[i][j])
    stack=[]
    for move in moves:
        i = move-1
        if dolls[i]:
            doll = dolls[i].pop()
            if stack:
                if stack[-1] == doll:
                    stack.pop()
                    answer+=1
                else:
                    stack.append(doll)
            else:
                stack.append(doll)
    return answer*2
