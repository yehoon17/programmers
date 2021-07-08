def solution(s, n):
    answer = ''
    for c in s:
        if c==' ':
            answer+=c
        else:
            i = ord(c)+n
            if ord(c)>=ord('a') and ord(c)<=ord('z'):
                if i>ord('z'):
                    i-=26
            else:
                if i>ord('Z'):
                    i-=26
            answer+=chr(i)
    return answer
