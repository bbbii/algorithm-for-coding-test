def solution(array):
    answer = 0
    array_list = ''.join(map(str, array))
    answer = array_list.count('7')
    return answer