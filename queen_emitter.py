def queen_emitter(board,queen_position_x,queen_position_y):
    for i in range(8):
        if board[i][queen_position_y] == 0:
            board[i][queen_position_y] = 1
        if board[queen_position_x][i] == 0:
            board[queen_position_x][i] = 1
        if queen_position_x - i >= 0:
            if queen_position_y + i <= 7:
                if board[queen_position_x-i][queen_position_y+i] == 0:
                    board[queen_position_x-i][queen_position_y+i] = 1
            if queen_position_y - i >= 0:
                if board[queen_position_x-i][queen_position_y-i] == 0:
                    board[queen_position_x-i][queen_position_y-i] = 1
        if queen_position_x + i <=7:
            if queen_position_y + i <= 7:
                if board[queen_position_x+i][queen_position_y+i] == 0:
                    board[queen_position_x+i][queen_position_y+i] = 1
            if queen_position_y - i >= 0:
                if board[queen_position_x+i][queen_position_y-i] == 0:
                    board[queen_position_x+i][queen_position_y-i] = 1
    return board
def queen_verifier(board):
    queens_position_list = []
    for row_index in range(len(board)):
        for item_index in range(len(board[row_index])):
            if board[item_index][row_index] == 1:
                board[item_index][row_index] = 0
            if board[item_index][row_index] == 'Q':
                temp = [item_index,row_index]
                queens_position_list.append(temp)
    for queen_position in queens_position_list:
        queen_emitter(board,queen_position[0],queen_position[1])
    return board



if __name__ == "__main__":
    chess_board = []
    for _ in range(8):
        chess_board.append([0] * 8)
    chess_board[0][0] = 'Q'
    chess_board[1][2] = 'Q'
    print(chess_board)
    chess_board2 = queen_emitter(chess_board,0,0)
    print(chess_board2)
    chess_board2 = queen_verifier(chess_board2)
    print(chess_board2)
