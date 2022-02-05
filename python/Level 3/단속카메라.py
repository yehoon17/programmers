def solution(routes):
    answer = 0

    routes.sort(key=lambda x: x[0], reverse=True)
    
    while routes:
        camera = min(routes, key=lambda x: x[1])[1]
        while routes[-1][0] <= camera:
            routes.pop()
            if not routes:
                break
        answer += 1

    return answer
