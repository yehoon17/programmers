def remove_all(pattern,string):
    while(pattern in string):
        string = string.replace(pattern,'')
    return string
    
def solution(string):
    answer = []
    for s in string:
        temp = '0'+ remove_all('110', s)
        count = (len(s) - len(temp) + 1)//3
        i = temp.rfind('0')
        s=temp[:i+1]+ '110'*count +temp[i+1:]
        answer.append(s[1:])
    return answer
