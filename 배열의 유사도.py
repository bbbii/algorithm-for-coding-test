def solution(s1, s2):
    answer = 0
    s1.extend(s2)
    for i in range(len(s1)):
        if s1.count(s1[i]) > 1:
            answer += 1
    return answer//2