def n_base_string(n, number):
    digits = "0123456789ABCDEF"[:n]
    num_str = ""

    while number > 0:
        num_str = digits[number % n] + num_str
        number //= n

    return num_str


def solution(n, t, m, p):
    seq = "0"
    number = 1
    while len(seq) < m*t:
        seq += n_base_string(n, number)
        number += 1

    return seq[p-1::m][:t]
