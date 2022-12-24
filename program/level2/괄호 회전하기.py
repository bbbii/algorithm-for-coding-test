def solution(s):
    answer = 0
    li = list(s) * 2
    for i in range(len(s)):
        stack = []
        idx = 0
        for j in range(len(s)):
            stack.append(li[i + j])
            idx += 1
            if idx >= 2:
                if stack[idx-2] + stack[idx-1] == '()' or stack[idx-2] + stack[idx-1] == '{}' or stack[idx-2] + stack[idx-1] == '[]':
                    del stack[idx-1]
                    del stack[idx-2]
                    idx = len(stack)
        if not stack:
            answer += 1
    return answer