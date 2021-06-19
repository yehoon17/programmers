def solution(answers):
    answer = []
    st1 = [1,2,3,4,5]
    st2 = [2,1,2,3,2,4,2,5]
    st3 = [3,3,1,1,2,2,4,4,5,5] 
    score1=0
    score2=0
    score3=0
    for i,a in enumerate(answers):
        if a == st1[i%5]:
            score1+=1
        if a == st2[i%8]:
            score2+=1
        if a == st3[i%10]:
            score3+=1
    m = max([score1,score2,score3])
    if m == score1:
        answer.append(1)
    if m == score2:
        answer.append(2)
    if m == score3:
        answer.append(3)
    return answer
