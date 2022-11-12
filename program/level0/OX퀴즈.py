def solution(quiz):
    i = 0
    answer = []
    dummy_str = []
    dummy_list = []
    while i < len(quiz):
        dummy_str = quiz[i]
        dummy_list = dummy_str.split(' = ')
        if eval(dummy_list[0]) == int(dummy_list[1]):
            answer.append("O")
        else:
            answer.append("X")
        i += 1
    return answer