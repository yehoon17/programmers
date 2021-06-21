def solution(lottos, win_nums):
    count = 0
    zero = 0
    for n in lottos:
        if n == 0:
            zero+=1
        else:
            if n in win_nums:
                count+=1
    highRank = 7-count-zero
    lowRank = 7-count
    if highRank>6:
        highRank=6
    if lowRank>6:
        lowRank=6
    return [highRank, lowRank]
