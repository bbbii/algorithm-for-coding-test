def solution(A, B):
    answer = 0
    C = A*2
    if B not in C:
        return -1
    elif A == B:
        return 0
    elif B in C:
        return len(B) - C.index(B)