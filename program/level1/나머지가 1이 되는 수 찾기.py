def solution(n):
    result = []
    for x in range(2, n):
        if n % x == 1:
            result.append(x)
    return min(result)