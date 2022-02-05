def solution(s):
    answer = []
    temp = s[2:-2].split('},{')
    temp.sort(key=lambda x: x.count(','))
    
    for x in temp:
        l = x.split(',')
        for i in l:
            if int(i) not in answer:
                answer.append(int(i))
                break

    return answer
