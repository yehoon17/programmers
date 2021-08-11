def solution(scores):
    answer = []
    for i, score in enumerate(scores):
        sum = get_sum(i, scores)
        avg = get_avg(i, sum, score)
        grade = get_grade(avg)
        answer.append(grade)
    return "".join(answer)

def get_sum(i, scores):
    temp = 0
    for score in scores:
        temp += score[i]
    return temp
            
def get_avg(i, sum, score):
    MAX = max(score)
    MIN = min(score)
    size = len(score)
    is_only_max = score[i] == MAX and score.count(MAX) == 1
    is_only_min = score[i] == MIN and score.count(MIN) == 1
    if is_only_max or is_only_min:
        return (sum - score[i]) / (size - 1)
    return sum / size 
        
def get_grade(avg):
    if avg < 50:
        return "F"
    elif avg < 70:
        return "D"
    elif avg < 80:
        return "C"
    elif avg < 90:
        return "B"
    return "A"
