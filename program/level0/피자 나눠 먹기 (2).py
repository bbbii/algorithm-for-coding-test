def solution(n):
    a = 1
    while 1:
        if (a*6) % n == 0:
            break
        a += 1
    return a