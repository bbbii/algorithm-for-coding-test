def solution(dots):
    x1 = []
    x2 = 0
    x3 = 0
    y1 = []
    y2 = 0
    y3 = 0
    for i in range(4):
        x1.append(dots[i][0])
    for j in range(2):
        y1.append(dots[j][1])
    x2 = max(x1)
    x3 = min(x1)
    y2 = max(y1)
    y3 = min(y1)
    return (x2-x3)*(y2-y3)