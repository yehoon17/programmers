def solution(price, money, count):
    need = price * count * (count + 1) // 2 - money
    return need if need > 0 else 0
