from collections import deque
def solution(prices):
    answer = []
    dq = deque(prices)
    while (dq):
        price = dq.popleft()
        cnt = 0
        for i in dq: 
            cnt += 1
            if price > i:
                break
        answer.append(cnt)
    return answer