def solution(board, moves):
    box = []
    delete = 0
    for i in moves :
        for j in range(len(board[1])):
            if board[j][i-1] != 0 :
                box.append(board[j][i-1])
                board[j][i-1] = 0 
                break
        if len(box) >= 2 and box[-1] == box[-2]:
            box.pop()
            box.pop()
            delete += 2
    return delete