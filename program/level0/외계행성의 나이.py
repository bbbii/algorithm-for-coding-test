def solution(age: int) -> str:
    dict = {index: chr(x) for index, x in enumerate(range(97, 97+10))}
    return ''.join(map(str, [dict[int(x)] for x in list(str(age))]))