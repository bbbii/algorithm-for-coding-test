def solution(price, money, count):
    sum_price = 0
    for i in range(1, count + 1):
        sum_price += price * i
    if money >= sum_price:
        return 0
    else:
        return sum_price - money