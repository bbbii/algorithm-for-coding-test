def solution(sides):
    answer = 0
    a = max(sides) - min(sides)
    b = max(sides) + min(sides)
    return b - a - 1