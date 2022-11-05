def solution(numbers, k):
    l = len(numbers)
    answer = numbers[2*(k-1)%l]
    return answer