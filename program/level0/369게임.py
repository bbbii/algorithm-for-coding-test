def solution(order):
    answer = 0
    a = str(order)
    answer = a.count('3')+a.count('6')+a.count('9')
    return answer