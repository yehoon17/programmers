def f(x, d):
    if x[0] == 'Enter':
        action = '들어왔'
    else:
        action = '나갔'
    return d[x[1]]+'님이 '+action+'습니다.'


def solution(record):
    arg = []
    d = {}
    for log in record:
        temp = log.split()
        if not temp[0][0] == 'C':
            arg.append(temp[:2])
        if not temp[0][0] == 'L':
            uid = temp[1]
            nick = temp[2]
            d[uid] = nick
            
    return [f(x, d) for x in arg]
