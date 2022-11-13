def solution(balls, share):
    a, b, c = 1, 1, 1
    for i in range(balls, 0, -1):
        a *= i
    for i in range(balls-share, 0, -1):
        b *= i
    for i in range(share, 0, -1):
        c *= i
    return a // (b * c)