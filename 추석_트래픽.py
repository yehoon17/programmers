def solution(lines):
    logStart = []
    logEnd = []
    for line in lines:
        _, time, period = line.split()
        endSec = 1000*(int(time[:2])*3600+int(time[3:5])*60+int(time[6:8]))+int(time[-3:])
        startSec = endSec+1-int(1000*float(period[:-1]))
        logStart.append(startSec)
        logEnd.append(endSec)
    logEnd.sort()
    logStart.sort()
    answer = 0
    i = 0
    count = 0
    for intervalEnd in logStart:
        count+=1
        intervalStart = intervalEnd-999
        while(True):
            if intervalStart>logEnd[i]:
                count-=1
                i+=1
            else:
                break
        answer=max(answer,count)
    return answer
