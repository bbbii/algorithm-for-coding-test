def solution(i, j, k):
    num_list = []
    answer = 0
    for x in range(i, j+1):
        num_list.append(x)
    num_str = ''.join(str(s) for s in num_list)
    answer = num_str.count(str(k))
    return answer