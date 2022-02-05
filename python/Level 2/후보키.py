from itertools import combinations


def solution(relation):
    nrow = len(relation)
    ncol = len(relation[0])
    candidates = []

    for i in range(1, ncol+1):
        for comb in combinations(range(ncol), i):
            isvalid = True
            for candidate in candidates:
                if candidate.issubset(set(comb)):
                    isvalid = False
                    break
                
            if isvalid:
                s = {tuple([relation[i][j] for j in comb])
                     for i in range(nrow)}
                if len(s) == nrow:
                    candidates.append(set(comb))

    return len(candidates)
