def solution(dots):
    answer = 0
    list_x, list_y, list_z = [], [], []
    for i in range(4):
        for j in range(1, 4):
            if i < j:
                list_x.append(dots[i][0]-dots[j][0])
                list_y.append(dots[i][1]-dots[j][1])
    for k in range(6):
        list_z.append(list_x[k]/list_y[k])
    if list_z[0] == list_z[5] or list_z[1] == list_z[4] or list_z[2] == list_z[3]:
        return 1
    else:
        return 0