def solution(spell, dic):
    answer = 2
    sorted_spell = sorted(spell)
    for i in dic:
        if sorted(list(i)) == sorted_spell:
            answer = answer - 1
    return answer