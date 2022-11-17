def solution(babbling):
    from itertools import permutations, combinations
    answer = 0
    a, ret = ['aya','ye','woo','ma'], []
    for i in range(2, 5):
        for t in list(combinations(a, i)):
            ret += [''.join(s) for s in list(permutations(t))]
    for s in babbling:
        if s in ret + a:
            answer += 1
    return answer