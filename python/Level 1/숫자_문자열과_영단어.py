def solution(s):
    answer = ''
    i = 0
    nums = '0123456789'
    letters = ['zero', 'one', 'two', 'three', 'four',
               'five', 'six', 'seven', 'eight', 'nine']

    while i < len(s) :
        if s[i] in nums:
            answer += s[i]
            i += 1
        else:
            for n, letter in enumerate(letters):
                if s[i:].startswith(letter):
                    answer += str(n)
                    i += len(letter)
                    break
                
    return int(answer)
