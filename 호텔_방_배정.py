def solution(k, room_number):
    answer = []
    redirect = {}
    for request in room_number:
        requested = []
        while True:
            requested.append(request)
            redirect.setdefault(request, request)
            if request == redirect[request]:
                break
            request = redirect[request]
            
        answer.append(request)
        available = request + 1
        for request in requested:
            redirect[request] = available
            
    return answer
