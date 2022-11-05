def solution(numbers):
    sort_num = sorted(numbers)
    a = sort_num[-1]*sort_num[-2]
    b = sort_num[0]*sort_num[1]
    return max(a, b)