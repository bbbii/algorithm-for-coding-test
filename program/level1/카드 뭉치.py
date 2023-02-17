def solution(cards1, cards2, goal):
    idx1, idx2, idx = 0, 0, 0
    while idx < len(goal):
        if cards1[idx1] == goal[idx]:
            idx += 1
            if idx1 < len(cards1) - 1:
                idx1 += 1
        elif cards2[idx2] == goal[idx]:
            idx += 1
            if idx2 < len(cards2) - 1:
                idx2 += 1
        else:
            return "No"
    return "Yes"