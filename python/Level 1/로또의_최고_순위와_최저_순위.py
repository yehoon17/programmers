def solution(lottos, win_nums):
    count = 0
    zero = 0
    for n in lottos:
        if n == 0:
            zero += 1
        else:
            if n in win_nums:
                count += 1

    highRank = min(6, 7 - count - zero)
    lowRank = min(6, 7 - count)

    return [highRank, lowRank]
