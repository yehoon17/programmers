def solution(m, musicinfos):
    answer = ''
    for musicinfo in musicinfos:
        start, end, title, chord = musicinfo.split(',')
        playtime = (int(end[:2])-int(start[:2]))*60+int(end[-2:])-int(start[-2:])
        music = chord*(playtime//len(chord))+chord[:playtime%len(chord)]
        if m in music:
            return title
    return answer
