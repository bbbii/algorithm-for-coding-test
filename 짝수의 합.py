def solution(n):
    Sum = 0
    0 < n <= 1000
    for i in range(1, n+1):
        if i%2 == 0:
            Sum += i
    answer = Sum
    return answer