def solution(k, m, score):
    answer = 0
    a = sorted(score)
    a.reverse()
    for i in range(0, len(a), m):
        b = a[i:i + m]
        if len(b) == m:
            answer += min(b) * len(b)
    return answer