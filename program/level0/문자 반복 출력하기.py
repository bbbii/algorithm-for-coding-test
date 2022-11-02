def solution(my_string, n):
    islist = []
    answer = ''
    for i in range(len(my_string)):
        islist.append(my_string[i]*n)
        answer = ''.join(j for j in islist)
    return answer