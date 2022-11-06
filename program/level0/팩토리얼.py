def solution(n):
    answer = 0
    i = 1
    while n > 0:
        n = n // i
        answer += 1
        i += 1
    return answer-1