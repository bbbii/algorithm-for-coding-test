def solution(my_str, n):
    answer = []
    a = len(my_str)/n
    b = len(my_str)//n
    c = 0
    count = 0
    if a >= b:
        c = a
    else:
        c = a+1
    while count < c:
        answer.append(my_str[:n])
        my_str = my_str[n:]
        count += 1
    return answer