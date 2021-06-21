def solution(nums):
    choose = len(nums)//2
    kind = len(set(nums))
    return min(choose, kind)
