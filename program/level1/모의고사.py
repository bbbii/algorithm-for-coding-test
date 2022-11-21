def solution(answers):
    answer = []
    i, count1, count2, count3 = 0, 0, 0, 0
    i1 = [1, 2, 3, 4, 5]
    i2 = [2, 1, 2, 3, 2, 4, 2, 5]
    i3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    while i < len(answers):
        if i1[i%5] == answers[i]:
            count1 += 1
        if i2[i%8] == answers[i]:
            count2 += 1
        if i3[i%10] == answers[i]:
            count3 += 1
        i += 1
    countlist = [count1, count2, count3]
    answercount = max(count1, count2, count3)
    for i in range(len(countlist)):
        if countlist[i] == answercount:
            answer.append(i+1)
    return answer
