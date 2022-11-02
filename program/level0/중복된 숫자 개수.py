def solution(array, n):
    Count = 0
    0 <= n <= 1000
    1 <= len(array) <= 100
    for i in array:
        0 <= i <= 1000
        if i == n:
            Count += 1
    return Count