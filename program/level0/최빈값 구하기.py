def solution(array):
    count_list = []
    for i in array:
        count_list.append(array.count(i))
    if count_list.count(max(count_list)) == max(count_list):
        return array[count_list.index(max(count_list))]
    else:
        return -1