def solution(n, words):
    store = [words[0]]
    for i in range(1, len(words)):
        store.append(words[i])
        for j in range(len(store) - 1):
            if store[i] == store[j]:
                return [(i % n) + 1, (i // n) + 1]
            if store[i][0] != store[i - 1][-1]:
                return [(i % n) + 1, (i // n) + 1]
    return [0, 0]