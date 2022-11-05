def solution(my_string):
    answer = ''
    a = ''
    for i in range(len(my_string)):
        if ord(my_string[i]) < 95: #대문자라면
            a += chr(ord(my_string[i]) + 32)
        elif ord(my_string[i]) > 95:
            a += chr(ord(my_string[i]) - 32)
    return a