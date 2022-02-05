def expend(num):
    return int((num*4)[:4])


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=expend)

    return str(int("".join(numbers)))
