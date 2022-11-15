def solution(phone_number):
    count = len(phone_number) - 4
    return "*" * count + phone_number[-4:]