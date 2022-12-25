from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    days = deque()
    for i in range(len(progresses)):
        tp = divmod(100 - progresses[i], speeds[i])
        if tp[1] == 0:
            days.append(tp[0])
        else:
            days.append(tp[0] + 1)
    print(days)
    cnt = 1
    while days:
        if cnt > 1:
            cnt -= 1 
            now_progres = days.popleft()
            continue
        now_progres = days.popleft()
        for progres in days: 
            if now_progres >= progres:
                cnt += 1 
            else:
                break
        answer.append(cnt)
    return answer