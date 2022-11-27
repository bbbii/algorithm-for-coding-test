def solution(n):
    a = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in a:
            a -= set(range(2 * i, n + 1, i))
    return n - len(a) - 1