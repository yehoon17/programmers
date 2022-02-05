def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    top = max(food_times)
    bot = min(food_times) - 1

    while bot + 1 < top:
        mid = (top + bot) // 2
        total = sum([min(t, mid) for t in food_times])
        if total > k:
            top = mid
        else:
            bot = mid

    k -= sum([min(t, bot) for t in food_times])
    temp = [1 if t > bot else 0 for t in food_times]
    start = 0
    end = len(food_times)

    while start + 1 < end:
        mid = (start + end) // 2
        total = sum(temp[:mid])
        if total > k:
            end = mid
        else:
            start = mid

    return start + 1
    