def binarySearch(nums, target):
    size = len(nums)
    if nums[-1]>=target:
        return size
    start = 0
    end = size-1
    while(not start > end):
        mid = int((start+end)/2)
        if nums[mid] == target:
            index = mid
            break
        elif nums[mid] < target:
            end = mid-1
        else:
            start = mid+1
    else:
        index = start
        
    while(nums[index]>=target):
        index+=1
    return index
            
    

def solution(info, query):
    answer = []
    
    d = {}
    for lang in ('cpp', 'java', 'python'):
        d[lang] = {}
        for job in ('backend','frontend'):
            d[lang][job] = {}
            for exp in ('junior','senior'):
                d[lang][job][exp] = {}
                for food in ('chicken','pizza'):
                    d[lang][job][exp][food] = []
    
    for x in info:
        xlist = x.split()
        d[xlist[0]][xlist[1]][xlist[2]][xlist[3]].append(int(xlist[4]))
    
    for d1 in d.values():
        for d2 in d1.values():
            for d3 in d2.values():
                for li in d3.values():
                    li.sort(reverse = True)
    
    for q in query:
        temp = q.split()
        count = 0
        qlist = [temp[i*2] for i in range(4)]
        qscore = int(temp[-1])
        temp = [d]
        for i in range(4):
            if qlist[i] == '-':
                temp = [t[k] for t in temp for k in t]
            else:
                temp = [t[qlist[i]] for t in temp]
        for t in temp:
            if not t == []:
                count += binarySearch(t,qscore)
        answer.append(count)
    
    return answer
