def solution(ingredient):
    idx, answer = 0, 0
    while idx < len(ingredient) - 3:
        if ingredient[idx:idx + 4] == [1, 2, 3, 1]:
            del ingredient[idx:idx + 4]
            idx -= 3
            answer += 1
            continue
        idx += 1
    return answer