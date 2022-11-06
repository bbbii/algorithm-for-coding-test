def solution(num_list, n):
    answer = []
    for i in range(len(num_list)//n):
        answer.append([])
        for j in range(n):
            answer[i].append(num_list[i*n+j])
    return answer