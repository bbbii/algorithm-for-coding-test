def solution(n):
    number = list(map(int, str(n)))
    number.sort()
    number.reverse()
    answer = ''.join(str(s) for s in number)
    return int(answer)