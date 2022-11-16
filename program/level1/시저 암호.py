def solution(s, n):
    password = list(s)
    answer = []
    for i in range(len(s)):
        if 65 <= ord(password[i]) <= 90:
            if ord(password[i]) + n > 90:
                answer.append(chr(ord(password[i]) + n - 26))
            else:
                answer.append(chr(ord(password[i]) + n))
        elif 97 <= ord(password[i]) <= 122:
            if ord(password[i]) + n > 122:
                answer.append(chr(ord(password[i]) + n - 26))
            else:
                answer.append(chr(ord(password[i]) + n))
        else:
            answer.append(' ')
    return ''.join(map(str, answer))