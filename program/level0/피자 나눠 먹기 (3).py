def solution(slice, n):
    2 <= slice <= 10
    1 <= n <= 100
    answer = (n-1)//slice + 1
    return answer