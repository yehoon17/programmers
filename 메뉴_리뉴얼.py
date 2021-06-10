from itertools import combinations

def solution(orders, course):
    answer = []
    li=[]
    for order in orders:
        temp = sorted(order)
        li.append(temp)
    for n in course:
        d = {}
        for order in li:
            for comb in combinations(order,n):
                temp = ''
                for c in comb:
                    temp+=c
                if temp in d:
                    d[temp] += 1
                else:
                    d[temp] = 1
        num = 2
        temp = []
        for k, v in d.items():
            if v>num:
                num = v
                temp = [k]
            elif v == num:
                temp.append(k)
        
        
        answer+=temp
    answer.sort()
    return answer
