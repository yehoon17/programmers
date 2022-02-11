def k_base_string(n, k):
    num_str = ""

    while n > 0:
        num_str = str(n % k) + num_str
        n //= k

    return num_str


def count_prime(numbers):
    cnt = 0
    for number in numbers:
        if number and number != "1":
            num = int(number)
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    break
            else:
                cnt += 1

    return cnt


def solution(n, k):
    num_str = k_base_string(n, k)
    candidates = num_str.split('0')
    return count_prime(candidates)
