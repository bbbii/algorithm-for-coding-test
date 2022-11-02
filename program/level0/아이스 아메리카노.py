def solution(money):
    0 < money <= 1000000
    a = money//5500
    b = money%5500
    answer = [a, b]
    return answer