def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        try:
            start = cache.index(city)
            for i in range(start, len(cache) - 1):
                cache[i] = cache[i+1]
            cache[-1] = city
            answer+=1
        except:
            answer+=5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                for i in range(len(cache) - 1):
                    cache[i] = cache[i+1]
                cache[-1] = city
                
    return answer
