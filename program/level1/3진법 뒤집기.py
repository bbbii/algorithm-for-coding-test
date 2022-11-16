def solution(n):
    num = ''
    while n > 0:
        n, m = divmod(n, 3)
        num += str(m)
    return int(num, 3)