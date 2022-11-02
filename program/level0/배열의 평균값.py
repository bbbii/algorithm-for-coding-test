def solution(numbers):
    for x in numbers:
        0 <= x <= 1000
    1 <= len(numbers) <= 100
    answer = sum(numbers)/len(numbers)
    return answer