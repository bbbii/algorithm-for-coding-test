from itertools import combinations
def solution(nums):
    comlist = []
    answer = 0
    for i in combinations(nums, 3):
        comlist.append(sum(i))
    for i in comlist:
        for j in range(2, i):
            if i % j == 0:
                break
            elif i == j + 1:
                answer += 1
    return answer