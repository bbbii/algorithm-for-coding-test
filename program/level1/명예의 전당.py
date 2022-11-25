def solution(k, score):
    count = 0
    b = score[:k]
    answer = []
    for i in score:
        count += 1
        if count <= k:
            a = sorted(score[:count])
            answer.append(a[0])
        elif count > k:
            b.append(score[count-1])
            b.sort()
            answer.append(b[count-k])
    return answer