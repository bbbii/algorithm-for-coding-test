def solution(s):
    count, zero = 0, 0
    while s != '1':
        zero += s.count('0')
        one = s.count('1')
        s = format(one, 'b')
        count += 1
    return [count, zero]