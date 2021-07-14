def solution(cacheSize, cities):
    answer = 0
    cache = {}
    temp = 0
    for i, city in enumerate(cities):
        city = city.lower()
        if city in cache:
            if cache[city] > i-cacheSize-1-temp:
                answer+=1
                temp+=1
            else:
                answer+=5
                temp=0
        else:
            answer+=5
        cache[city] = i
    return answer
