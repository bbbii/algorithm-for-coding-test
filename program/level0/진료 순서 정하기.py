def solution(emergency):
    answer = []
    s_emergency = sorted(emergency)
    s_emergency.reverse()
    for i in range(len(emergency)):
        answer.append(s_emergency.index(emergency[i])+1)
    return answer