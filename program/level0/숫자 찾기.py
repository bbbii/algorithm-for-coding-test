def solution(num, k):
    answer = 0
    a = str(num)
    b = str(k)
    c = a.find(b)
    if c != -1:
        return c + 1
    else:
        return c