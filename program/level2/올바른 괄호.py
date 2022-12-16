def solution(s):
    count = 0
    for i in s:
        if i == ")":
            count -= 1
        else:
            count += 1
        if count < 0:
            return False
            break
    if count == 0:
        return True
    elif count > 0:
        return False