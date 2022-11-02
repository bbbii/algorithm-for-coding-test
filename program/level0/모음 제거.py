def solution(my_string):
    a = my_string.replace("a", "")
    b = a.replace("e", "")
    c = b.replace("i", "")
    d = c.replace("o", "")
    e = d.replace("u", "")
    return e