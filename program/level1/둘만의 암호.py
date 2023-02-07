def get_skip_alpha_list(skip):
    return [chr(alpha_num) for alpha_num in range(ord('a'), ord('z') + 1) if chr(alpha_num) not in skip]

def shift_alpha(alpha, index, skip_alpha_list):
    skip_alpha_len = len(skip_alpha_list)
    return skip_alpha_list[(skip_alpha_list.index(alpha) + index) % skip_alpha_len]

def solution(s, skip, index):    
    alpha_list = get_skip_alpha_list(skip)
    shift_s = "".join([
        shift_alpha(alpha, index, alpha_list) for alpha in list(s)
    ])
    return shift_s