from itertools import * 
def solution(numbers):
    sum_list = []
    perm_list = list(permutations(numbers, 2))
    for i in perm_list:
        sum_list.append(sum(i))
    return sorted(list(set(sum_list)))