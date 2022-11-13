def solution(a, b):
    q = []
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            a = a // i
            b = b // i
    for i in range(2, b + 1):
        if b % i == 0:
            q.append(i)
    for i in q:
        for j in range(2, 1001):
            if i * j in q:
                q.remove(i * j)
    s1 = set([2, 5])
    s2 = set(q)
    if s1 | s2 == s1:
        return 1
    else:
        return 2