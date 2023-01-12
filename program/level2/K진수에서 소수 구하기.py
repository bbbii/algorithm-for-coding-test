def prime_check(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    rev_base = ''
    answer = 0
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    rev_list = rev_base[::-1].split("0")
    for i in rev_list:
        if i and prime_check(int(i)):
            answer += 1
    return answer