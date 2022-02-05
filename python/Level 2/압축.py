def solution(msg):
    answer = []
    dic = {chr(ord('A')+i): i+1 for i in range(26)}
    val = 27

    i = 0
    while i < len(msg):
        n = 0
        while(i+n < len(msg)):
            key = msg[i:i+n+1]
            if key not in dic:
                break
            n += 1
            
        answer.append(dic[msg[i:i+n]])
        dic[key] = val
        val += 1
        i += n

    return answer
