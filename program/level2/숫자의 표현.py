def solution(n):
    num, answer = 0, 0
    for i in range(1, n + 2):
        num = 0
        for j in range(i, n + 2):
            if num < n:
                num += j
            elif num > n:
                break
            elif num == n:
                answer += 1
                break
    return answer