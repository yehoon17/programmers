def solution(k, room_number):
    answer = []
    redirect = {i: i for i in range(k+1)}
    for request in room_number:
        requested = []
        while True:
            requested.append(request)
            if request == redirect[request]:
                break
            request = redirect[request]
            
        answer.append(request)
        available = request + 1
        for request in requested:
            redirect[request] = available
            
    return answer
