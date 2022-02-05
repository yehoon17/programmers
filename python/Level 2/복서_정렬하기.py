def solution(weights, head2head):
    boxers = list(range(len(weights)))
    
    count = []
    for boxer in boxers:
        cnt = 0
        for i, total in enumerate(head2head[boxer]):
            if total == "W" and weights[boxer] < weights[i]:
                cnt += 1
        count.append(cnt)
        
    rate = []
    for boxer in boxers:
        if head2head[boxer].count("N") == len(weights):
            rate.append(0)
        else:
            rate.append(head2head[boxer].count("W")/(head2head[boxer].count("W")+head2head[boxer].count("L"))) 
            
    boxers.sort(key=lambda x: weights[x], reverse=True)
    boxers.sort(key=lambda x: count[x], reverse=True)
    boxers.sort(key=lambda x: rate[x], reverse=True) 
    return [boxer+1 for boxer in boxers]
