def solution(k, d):
    square = d ** 2
    return sum(int((square - i ** 2) ** .5) // k + 1 for i in range(0, d + 1, k))