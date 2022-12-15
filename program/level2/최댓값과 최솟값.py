def solution(s):
    a = []
    result = s.split()
    for i in result:
        a.append(int(i))
    return str(min(a)) + " " + str(max(a))