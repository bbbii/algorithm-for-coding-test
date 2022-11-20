def solution(array, commands):
    answer = []
    for i in commands:
        sliced_array = array[i[0] - 1:i[1]]
        sorted_arry = sorted(sliced_array)
        answer.append(sorted_arry[i[2] - 1])
    return answer