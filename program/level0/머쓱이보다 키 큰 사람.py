def solution(array, height):
    count = 0
    1 <= len(array) <= 100
    1 <= height <= 200
    for i in array:
        1 <= i <= 200
        if i > height:
            count += 1
    return count