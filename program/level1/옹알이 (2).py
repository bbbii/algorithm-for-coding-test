def solution(babbling):
    result = 0
    for word in babbling:
        stack = ''
        prev = ''
        for char in word:
            stack += char
            if prev != stack and (stack == 'aya' or stack == 'ye' or stack == 'woo' or stack == 'ma'):
                prev = stack
                stack = ''
        if len(stack) == 0:
            result += 1
    return result