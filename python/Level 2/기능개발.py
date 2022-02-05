def solution(progresses, speeds):
    answer = []
    p_stack = progresses[::-1]
    s_stack = speeds[::-1]
    days = 0
    while p_stack:
        speed = s_stack.pop()
        progress = p_stack.pop() + speed*days
        count = 1
        days += -1*((progress-100) // speed)
        while p_stack and p_stack[-1] + s_stack[-1]*days >= 100:
            p_stack.pop()
            s_stack.pop()
            count += 1

        answer.append(count)

    return answer
