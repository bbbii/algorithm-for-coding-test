def solution(n, k, enemy):
    from heapq import heappushpop, heappush
    heap = []
    total = round_ = 0
    for each in enemy:
        total += each
        if total <= n:
            heappush(heap, -each)
            round_ += 1
        elif k > 0:
            k -= 1
            total += heappushpop(heap, -each)
            round_ += 1
        else:
            break
    return round_