def solution(msg):
    answer = []
    dic = {chr(ord('A')+i):i+1 for i in range(26)}
    val = 27
    i, n = 0, 1
    while(i<len(msg)):
        key = msg[i:i+n]
        if key in dic:
            answer.append(dic[key])
            dic.pop(key)
            if i+n<len(msg):
                dic[msg[i:i+n+1]] = val
                val+=1
            i+=n
            n = 1
        else:
            n+=1
    return answer
