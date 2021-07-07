def solution(a, b):
    days=0
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(a-1):
        days+=month[i]
    days+=b
    weekday=['THU','FRI','SAT','SUN','MON','TUE','WED']
    return weekday[days%7]
