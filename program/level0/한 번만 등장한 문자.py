def solution(s):
    s_count = []
    dummy = []
    for i in range(len(s)):
        s_count.append(s.count(s[i]))
        if s_count[i] == 1:
            dummy.append(s[i])
    return ''.join(s for s in sorted(dummy))