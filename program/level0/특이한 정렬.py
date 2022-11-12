def solution(numlist, n):
    answer = [] 
    for i in numlist:
        if i >= n:
            distance = i - n 
        else:
            distance = n - i 
        answer.append([i, distance])
    answer.sort(key = lambda x : (x[1], -x[0]))
    return [i[0] for i in answer]