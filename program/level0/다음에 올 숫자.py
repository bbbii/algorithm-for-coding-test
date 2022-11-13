def solution(common):
    if common[0] - common[1] == common[1] - common[2]:
        return common[len(common)-1] + common[1] - common[0]
    else:
        return common[len(common)-1] * (common[1] // common[0])