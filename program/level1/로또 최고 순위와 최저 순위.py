def solution(lottos, win_nums):
    count = 0
    for i in lottos:
        if i in win_nums:
            count += 1
    return [7 - max(count + lottos.count(0), 1), 7 - max(count, 1)]