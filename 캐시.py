def solution(cacheSize, cities):
    answer = 0
    cache = {}
    for i, city in enumerate(cities):
        city = city.lower()
        if city in cache:
            if cache[city] > i-cacheSize-1:
                answer+=1
            else:
                answer+=5
        else:
            cache[city] = i
            answer+=5
    return answer
