def solution(n):
    count = 2
    arr = [0, 1]
    while len(arr) - 1 < n:
        arr.append(arr[count - 1] + arr[count - 2])
        count += 1
    return arr[n] % 1234567