def solution(n):
    x = 1
    a = format(n, 'b').count('1')
    while a != format(n + x, 'b').count('1'):
        x += 1
    return n + x