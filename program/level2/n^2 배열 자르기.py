def solution(n, left, right):
    arr = []
    i, j = left // n, left % n
    while len(arr) < right - left + 1:
        arr.append(max(i, j) + 1)
        if j == n - 1:
            j = 0
            i += 1
        else:
            j += 1
    return arr