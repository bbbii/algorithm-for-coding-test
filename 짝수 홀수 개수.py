def solution(num_list):
    a = len(num_list)
    b = 0
    for i in num_list:
        if i%2 == 0:
            b += 1
    c = a - b
    answer = [b, c]
    return answer