def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        for j in range(0, 10):
            if my_string[i] == str(j):
                answer.append(j)
                answer.sort()
    return answer