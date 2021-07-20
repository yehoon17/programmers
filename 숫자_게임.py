def solution(A, B):
    score = 0
    A.sort()
    B.sort()
    i,j = 0,0
    size = len(A)
    while(j<size):
        if B[j]>A[i]:
            score+=1
            i+=1
        j+=1
    return score
