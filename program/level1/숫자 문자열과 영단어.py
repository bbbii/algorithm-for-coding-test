def solution(s):
    answer, word = '', ''
    words = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for i in s:
        if i.isdigit():
            answer += i
            continue
        word += i
        if word in words:
            answer += words[word]
            word = ''
    return int(answer)