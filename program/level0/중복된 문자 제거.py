def solution(my_string):
    answer_list = []
    answer = ''
    index = []
    isindex = list(my_string)
    for i in range(len(my_string)):
        for j in range(i+1, len(my_string)):
            if my_string[i] == my_string[j]:
                index.append(j)
    for k in range(len(my_string)):
        if k not in index:
            answer_list.append(isindex[k])
            answer = ''.join(answer_list)
    return answer