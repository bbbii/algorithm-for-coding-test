def solution(t, p):
    x, answer = 0, 0
    li = []
    for i in range(len(t) - len(p) + 1):
        ex = len(p) - 1
        for j in range(len(p)):
            x += int(t[i + j]) * (10**(ex - j))
        li.append(x)
        x = 0
    for i in li:
        if i <= int(p):
            answer += 1
    return answer