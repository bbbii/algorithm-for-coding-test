def solution(sizes):
    width = 0
    height = 0

    for i in range(len(sizes)):
        sizes[i].sort()

    for i in range(len(sizes)):
        if width < sizes[i][0]:
            width = sizes[i][0]

    for i in range(len(sizes)):
        if height < sizes[i][1]:
            height = sizes[i][1]

    area = width * height
    return area