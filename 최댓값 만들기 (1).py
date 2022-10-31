def solution(numbers):
    2 <= len(numbers) <= 100
    for i in numbers:
        0 <= i <= 10000
    a = max(numbers)
    b = numbers.index(a)
    c = numbers.pop(b)
    d = max(numbers)
    answer = a*d
    return answer