def solution(rsp):
    answer = ''
    rsp_key = {'2':'0', '0':'5', '5':'2'}
    for i in list(rsp):
        answer += rsp_key[i]
    return answer