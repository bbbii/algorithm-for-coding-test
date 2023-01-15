def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0:
            answer.append(i + 1)
            continue
        bin_num = '0' + bin(i)[2:]
        bin_num = bin_num[:bin_num.rindex('0')] + '10' + bin_num[bin_num.rindex('0') + 2:]
        answer.append(int(bin_num, 2))
    return answer