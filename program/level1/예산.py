def solution(d, budget):
    sort_d = sorted(d)
    a, count = 0, 0
    for i in sort_d:
        if budget > a:
            count += 1
            a += i
            if budget < a:
                count -= 1
                a -= i
                break
        else:
            break
    return count