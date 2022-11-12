def solution(num, total):
    answer = []
    a = total//num
    if num % 2 == 1:
        for i in range(num):
            answer.append(a - num//2 + i)
    else:
        for i in range(num):
            answer.append(a - num//2 + i + 1)
    return answer