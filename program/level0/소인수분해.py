def solution(n):
    answer = []
    q = []
    for i in range(2, n+1):
        if n % i == 0:
            q.append(i)    
    for i in q:
        for j in range(2, 5000):
            if i * j in q:
                q.remove(i * j)
    q.sort()
    return q