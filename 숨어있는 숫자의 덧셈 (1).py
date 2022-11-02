def solution(my_string):
    answer = 0
    for i in range(len(my_string)):
        for j in range(1, 10):
            if my_string[i] == str(j):
                answer += j
    return answer