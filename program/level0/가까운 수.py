def solution(array, n):
    sorted_array = sorted(array)
    abs_array = []
    for i in sorted_array:
        abs_array.append(abs(i - n))
    x = abs_array.index(min(abs_array))
    return sorted_array[x]