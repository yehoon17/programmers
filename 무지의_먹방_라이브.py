def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    size = len(food_times)
    top = max(food_times)
    bot = min(food_times) - 1
    while True:
        mid = (top + bot) // 2
        total = sum([min(t, mid) for t in food_times])
        if total > k:
            top = mid
        else:
            bot = mid
        if bot + 1 >= top:
            break

    k -= sum([min(t, bot) for t in food_times])
    temp = [1 if t > bot else 0 for t in food_times]
    start = 0
    end = size
    while True:
        mid = (start + end) // 2
        total = sum(temp[:mid])
        if total > k:
            end = mid
        else:
            start = mid
        if start + 1 >= end:
            break
    return start + 1
