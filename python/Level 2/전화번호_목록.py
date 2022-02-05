# 메모: 효율성을 위해 먼저 정렬하고 비교하기

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True
