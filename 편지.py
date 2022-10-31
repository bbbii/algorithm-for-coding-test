def solution(message):
    a = []
    for i in message:
        a.append(i)
    if 1 <= len(a) <= 50:
        answer = len(a)*2
    return answer