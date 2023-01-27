from collections import Counter
def solution(topping):
    answer = 0
    total = Counter(topping)
    set1 = set()
    while len(topping) > 1:
        poped = topping.pop()
        set1.add(poped)
        if total[poped] > 1:
            total[poped] = total[poped] - 1
        else:
            del total[poped]
        if len(total) == len(set1):
            answer += 1
    return answer