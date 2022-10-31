def solution(denum1, num1, denum2, num2):
    0 < denum1, num1, denum2, num2 < 1000
    x = (denum1*num2 + denum2*num1)
    y = (num1*num2)
    z = gcd(x, y)
    answer = [x//z, y//z]
    return answer

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)