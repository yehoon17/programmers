def solution(n, k):
    answer=[]
    
    fact = [1]
    for i in range(1,n):
        fact.append(fact[-1]*i)
        
    nums = [False for _ in range(n)]
    
    for m in range(n):
        if fact[-1-m]==1:
            i=1
        else:
            i = k//fact[-1-m]+1
        for j,num in enumerate(nums):
            if not num:
                i-=1
            if i==0:
                answer.append(j+1)
                nums[j]=True
                break
        k = k%fact[-1-m]
        
    return answer
