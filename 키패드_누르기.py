def dist(a,b,d):
    return abs(d[a][0]-d[b][0]) + abs(d[a][1]-d[b][1])

def solution(numbers, hand):
    d={n:[(n-1)//3,(n+2)%3] for n in range(1,10)}
    d[-1] = [3,0]
    d[0] = [3,1]
    d[-2] = [3,2] 
    answer = ''
    thumbL = -1
    thumbR = -2
    hand = hand[0].upper()
    for n in numbers:
        if n in [1,4,7]:
            answer+='L'
            thumbL = n
        elif n in [3,6,9]:
            answer+='R'
            thumbR = n
        else:
            disL = dist(n,thumbL,d)
            disR = dist(n,thumbR,d)
            if disL < disR:
                answer+='L'
                thumbL = n
            elif disL > disR:
                answer+='R'
                thumbR = n
            else:
                answer+=hand
                if hand == 'R':
                    thumbR = n
                else:
                    thumbL = n
                    
    return answer
