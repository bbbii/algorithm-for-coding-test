from collections import Counter
def solution(N, stages):
    arrived = [0 for i in range(N+1)]
    percent = [0 for i in range(N)]
    answer = []
    for i in stages:
        for j in range(i):
            arrived[j] = arrived[j] + 1
    dict = Counter(stages)
    for i in range(N):
        if arrived[i] != 0:
            percent[i] = dict[i+1] / arrived[i]
    dict2 = {}
    for i in range(N):
        dict2[i + 1] = percent[i]
    sorted_dict = sorted(dict2.keys(), key = lambda item: dict2[item], reverse=True)
    return sorted_dict