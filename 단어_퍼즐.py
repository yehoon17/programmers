def f(i,t):
    if i==len(t):
        return 0
    m=len(t)
    for x in t[i]:
        m=min(m,f(i+x,t))
    return m+1

def solution(strs, t):
    temp = [[] for _ in t]
    for start in range(len(t)):
        for pat in strs:
            size=len(pat)
            if start+size<=len(t):
                if pat == t[start:start+size]:
                    temp[start].append(size)
    answer=f(0,temp)
    if answer>len(t):
        return -1
    return answer
