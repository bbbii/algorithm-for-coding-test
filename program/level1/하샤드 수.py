def solution(x):
    answer = 0
    number = str(x)
    for i in range(len(number)):
        answer += int(number[i])
    if x % answer == 0:
        return True
    else:
        return False