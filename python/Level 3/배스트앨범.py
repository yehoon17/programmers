def solution(genres, plays):
    answer = []

    total_plays_of = {genre: 0 for genre in set(genres)}
    for genre, play in zip(genres, plays):
        total_plays_of[genre] += play

    topTwo = {}
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
    
        if g in topTwo:
            temp = topTwo[g]
            if len(temp) == 1:
                if temp[0][1] > p:
                    temp.append([i, p])
                else:
                    t = [[i, p], temp[0]]
                    topTwo[g] = t
            else:
                if temp[0][1] < p:
                    t = [[i, p], temp[0]]
                    topTwo[g] = t
                elif temp[1][1] < p:
                    temp[1] = [i, p]
        else:
            topTwo[g] = [[i, p]]
            
    keys = list(total_plays_of.keys())
    keys.sort(key=lambda x: total_plays_of[x], reverse=True)
    for k in keys:
        for i in range(len(topTwo[k])):
            answer.append(topTwo[k][i][0])

    return answer
