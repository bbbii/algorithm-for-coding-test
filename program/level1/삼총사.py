from itertools import *
def solution(number):
    answer = 0
    comb_list = list(combinations(number, 3))
    for i in comb_list:
        if sum(i) == 0:
            answer += 1
    return answer