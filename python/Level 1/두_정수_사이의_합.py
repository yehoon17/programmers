def solution(a, b):
    large = max(a, b)
    small = min(a, b)
    return int((small+large)*(1+large-small)/2)
