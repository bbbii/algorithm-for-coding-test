def solution(s):
    answer = []
    for i in range(len(s)):
        if s[:i + 1].count(s[i]) == 1:
            answer.append(-1)
        for j in reversed(range(i)):
            if s[i] == s[j]:
                answer.append(i - j)
                break
    return answer