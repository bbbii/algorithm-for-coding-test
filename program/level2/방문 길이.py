def solution(dirs):
    answer, x, y = 0, 5, 5
    now = []
    dic = {'U':(0,-1),'D':(0,1),'R':(1,0),'L':(-1,0)}
    for i in range(len(dirs)):
        (dy, dx) = dic[dirs[i]]
        if not (0 <= x + dx and x + dx <= 10 and 0 <= y + dy and y + dy <= 10):
            continue
        now.append((x, y, x + dx, y + dy))
        now.append((x + dx, y + dy ,x , y))
        x = x + dx
        y = y + dy
    mapSet = set(now)
    answer = len(mapSet) // 2
    return answer