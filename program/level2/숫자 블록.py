def solution(begin, end):
    answer = []
    for i, num in enumerate(range(begin, end+1)):
        t_max = 1
        for yak in range(2, int(num ** 0.5)+1):
            if num % yak == 0:
                t_max = num // yak
                if t_max > 10000000:
                    t_max = 1
                    continue
                else:
                    break
        answer.append(t_max)
    if begin == 1:
        answer[0] = 0
    return answer