import itertools
def solution(clothes):
    answer = 1
    li = []
    for i in range(len(clothes)):
        li.append(clothes[i][1])
    ctype = set(li)
    count = []
    for i in ctype:
        count.append(li.count(i))
    for i in range(len(count)):
        answer *= (count[i] + 1)
    return answer - 1