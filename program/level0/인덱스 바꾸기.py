def solution(my_string, num1, num2):
    index1 = my_string[num1]
    index2 = my_string[num2]
    slicing1 = my_string[:num1]
    slicing2 = my_string[num1+1:num2]
    slicing3 = my_string[num2+1:]
    answer = slicing1+index2+slicing2+index1+slicing3
    return answer