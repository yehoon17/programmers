import numpy as np

def solution(key, lock):
    M = len(key)
    N = len(lock)
    key = np.array(key)
    lock = np.array(lock)
    lock = np.pad(lock,M-1,'constant')
    ones = np.ones((N,N))
    
    for x in range(M+N-1):
        for y in range(M+N-1):
            for i in range(4):
                k = np.rot90(key,i)
                lock[x:x+M,y:y+M]+=k
                if np.array_equal(lock[M-1:M-1+N,M-1:M-1+N],ones):
                    return True
                lock[x:x+M,y:y+M]-=k
        
    return False
