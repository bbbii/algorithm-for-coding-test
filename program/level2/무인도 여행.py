import sys
sys.setrecursionlimit(10 ** 5)

def solution(maps):
    converted_map = [list(val) for val in maps]
    rows = len(converted_map)
    cols = len(converted_map[0])
    for r in range(rows):
        for c in range(cols):
            if converted_map[r][c] == "X":
                converted_map[r][c] = 0
            else:
                converted_map[r][c] = int(converted_map[r][c])
    seen = set()
    def dfs(r, c):
        if (r < 0 or c < 0 or (r,c) in seen or r == rows or c == cols or converted_map[r][c] == 0):
            return 0
        seen.add((r, c))
        return (converted_map[r][c] + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
    areas, ans = [], []
    for r in range(rows):
        for c in range(cols):
            areas.append(dfs(r, c))
    if sum(areas) == 0:
        return [-1]
    for area in areas:
        if area != 0:
            ans.append(area)
    ans.sort()
    return ans