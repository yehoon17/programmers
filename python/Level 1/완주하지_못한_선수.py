def solution(participant, completion):
    cnt = {name: 0 for name in set(participant)}
    for name in completion:
        cnt[name] += 1

    for name in participant:
        cnt[name] -= 1
        if cnt[name] < 0:
            return name
