def solution(sticker):
    size = len(sticker)
    if size < 4:
        return max(sticker)

    x_x = sticker[1]
    o_x = sticker[0]
    x_o = sticker[2]
    o_o = sticker[0]+sticker[2]

    for i in range(3, size):
        temp = max(x_x, x_o)
        x_o = x_x + sticker[i]
        x_x = temp
        temp = max(o_x, o_o)
        o_o = o_x + sticker[i]
        o_x = temp

    return max(x_x, o_x, x_o)
