def solution(n, k):
    0 <= n < 1000
    n/10 <= k < 1000
    price = n*12000 + k*2000 - (n//10)*2000
    return price