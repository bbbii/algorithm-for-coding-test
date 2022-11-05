def solution(bin1, bin2):
    dec1 = int(bin1, 2)
    dec2 = int(bin2, 2)
    dec_sum = dec1 + dec2
    answer = bin(dec_sum)[2:]
    return answer