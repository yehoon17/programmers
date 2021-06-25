def solution(enroll, referral, seller, amount):
    size = len(enroll)
    answer=[0 for _ in range(size)]
    d={k:v for k,v in zip(enroll, referral)}
    index={enroll[i]:i for i in range(size)}
    for s,n in zip(seller,amount):
        cost = n*100
        x = s
        while(True):
            refer = d[x]
            temp = cost//10
            answer[index[x]]+=cost-temp
            cost=temp
            if cost == 0:
                break
            x = refer
            if x=='-':
                break
    return answer
