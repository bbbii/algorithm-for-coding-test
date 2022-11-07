def solution(s):
    answer = 0
    stack =[]
    for i in s.split():
        stack.append(i)
        if i == 'Z':
            stack.pop()
            if len(stack)>=1:
                stack.pop()
    for i in stack:
        answer += int(i)
    return answer