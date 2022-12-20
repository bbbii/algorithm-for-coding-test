def solution(brown, yellow):
    num = []
    for i in range(1, brown + yellow + 1):
        if (brown + yellow) % i == 0:
            num.append(i)
    for x in num:
        y = (brown + yellow) // x
        if (x - 2) * (y - 2) == yellow and x >= y:
            return [x, y]