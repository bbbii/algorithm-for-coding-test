def solution(s):
    s_lower = s.lower()
    if s_lower.count('p') == s_lower.count('y'):
        return True
    else:
        return False