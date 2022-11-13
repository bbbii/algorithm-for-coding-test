def solution(chicken):
    answer = 0
    a = []
    while chicken > 9:
        a = list(divmod(chicken, 10)) #a(1)
        chicken = a[0] + a[1]
        answer += a[0]
    return answer