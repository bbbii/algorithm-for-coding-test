def solution(array):
    answer = 0
    array.sort()
    a = len(array)%2
    if a == 0:
        return array[len(array)//2-1]
    else:
        return array[len(array)//2]