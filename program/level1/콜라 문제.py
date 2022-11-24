def solution(a, b, n):
    x, y, answer = 0, 0, 0
    while n >= a:
        x, y = list(divmod(n, a))
        answer += b * x
        n = b * x + y
    return answer