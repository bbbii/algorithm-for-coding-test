def solution(elements):
    elements2 = elements * 2
    li = []
    for i in range(len(elements)):
        for j in range(len(elements) - 1):
            li.append(sum(elements2[i:i + j + 1]))
    return len(set(li)) + 1