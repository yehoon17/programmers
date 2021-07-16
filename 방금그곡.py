def modify(x):
    i=0
    x_=''
    while(i<len(x)-1):
        if x[i+1]=='#':
            x_+=x[i].lower()
            i+=2
        else:
            x_+=x[i]
            i+=1
        if i==len(x)-1:
            x_+=x[i]
    return x_
    

def solution(m, musicinfos):
    answer = ''  
    m_=modify(m)
    for musicinfo in musicinfos:
        start, end, title, chord = musicinfo.split(',')
        chord_=modify(chord)
        playtime = (int(end[:2])-int(start[:2]))*60+int(end[-2:])-int(start[-2:])
        music = chord_*(playtime//len(chord_))+chord_[:playtime%len(chord_)]
        if m_ in music:
            return title
    return answer
