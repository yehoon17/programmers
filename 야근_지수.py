def solution(n, works):
    if sum(works)<n:
        return 0
    size=len(works)
    works.sort()
    works.append(0)
    temp = -n
    x=size
    for i in range(1,size):
        temp+=i*(works[size-i]-works[size-i-1])
        if temp >= 0:
            x = i
            break
    if size==x:
        temp=sum(works)-n
    a,b = temp//x,temp%x
    for i in range(size-x,size):
        works[i] = works[size-x-1]+a
    for i in range(size-b,size):
        works[i]+=1
    answer=0
    for work in works:
        answer+=work*work
    return answer
