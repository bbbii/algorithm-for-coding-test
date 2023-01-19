def solution(orders, course):
    answer = []
    for i in range(len(orders)):
        answer.append([])
        for j in range(len(orders[i])):
            answer[i].append(orders[i][j])
    for i in range(len(answer)):
        for j in range(len(answer[i])-1):
            for z in range(j+1,len(answer[i])):
                if answer[i][j] in answer[i][z]:
                    continue
                answer[i].append(answer[i][j]+answer[i][z])
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            answer[i][j] = sorted(answer[i][j])
    allrecord = []
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            if answer[i][j] in answer[i][:j]:
                continue
            allrecord.append(answer[i][j])
    answer2 = []
    for i in allrecord:
        if i not in answer2:
            answer2.append(i)
    len_case = []
    for i in course:
        len_case.append([])
        for j in answer2:
            if i == len(j):
                len_case[-1].append(j)
    len_case2 = []
    max_cnt = 2
    for i in len_case:
        for j in i:
            if allrecord.count(j) > max_cnt:
                max_cnt = allrecord.count(j)
        len_case2.append([])
        for j in i:
            if allrecord.count(j) == max_cnt and j not in len_case2[-1]:
                len_case2[-1].append(j)
        max_cnt = 2
    last = []
    for i in len_case2:
        for j in i:
            last.append("".join(j))
    return sorted(last)