def solution(string):
    answer = []
    for s in string:
        temp = ['0']
        for c in s:
            temp.append(c)
            if temp[-3:] == ['1','1','0']:
                    temp.pop()
                    temp.pop()
                    temp.pop()
        temp = ''.join(temp)
        count = (len(s) - len(temp) + 1)//3
        i = temp.rfind('0')
        s=temp[:i+1]+ '110'*count +temp[i+1:]
        answer.append(s[1:])
    return answer
