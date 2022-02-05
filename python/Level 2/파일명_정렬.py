def solution(files):
    temp = {}

    for f in files:
        i = 0
        head = ''
        while i < len(f):
            if f[i] in '0123456789':
                break
            head += f[i].lower()
            i += 1

        numstr = ''
        while i < len(f):
            if f[i] not in '0123456789':
                break
            numstr += f[i]
            i += 1
            
        number = int(numstr)
        temp[f] = [head, number]

    files.sort(key=lambda x: temp[x][1])
    files.sort(key=lambda x: temp[x][0])

    return files
