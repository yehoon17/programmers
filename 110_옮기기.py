def solution(string):
    answer = []
    for s in string:
        temp = s
        while('110' in temp):
            temp = temp.replace('111100','')
            temp = temp.replace('110','')
            temp = temp.replace('110','')
        temp = '0' + temp
        count = (len(s) - len(temp) + 1)//3
        i = temp.rfind('0')
        s=temp[:i+1]+ '110'*count +temp[i+1:]
        answer.append(s[1:])
    return answer
