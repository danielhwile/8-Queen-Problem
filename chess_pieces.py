import queen_emitter
def create_board():
    '''This function creates our chess board, a board of 8 rows of 8 zeros'''
    board = []
    for _ in range(8):
        board.append([0] * 8)
    return board

def queen_placer(board,test_row=0):
    '''This function will actually place a queen on the board for the row test_row
    then it will either step to the previous row and move a queen or it will go to the next row and place a queen'''
    remaining_options_check_count = 0
    for row in board:
        for item in row:
            if item == 0:
                remaining_options_check_count += 1
    #This first Section of code above tests that there are still places remaining for queens to be placed
    if remaining_options_check_count == 0 and test_row == 7:
        return queen_placer(board,test_row-1)
    '''The lines above check that if we are on the final row, and there is nowhere remaining to place any Queens that we 
    move back 1 row and attempt to move the queen'''
    for item_index in range(len(board[test_row])):
        if board[test_row][item_index] == "Q":
            board[test_row][item_index] = 0
            queen_emitter.queen_verifier(board)
            for cont_index in range(item_index+1,8):
                if board[test_row][cont_index] == 0:
                    board[test_row][cont_index] = 'Q'
                    queen_emitter.queen_verifier(board)
                    return queen_placer(board, test_row+1)
            return queen_placer(board,test_row-1)
    '''This loop above checks whether a queen is already in the row we are calling, this tells us if this is the first 
    time we are attempting to place a queen in the row
    if a queen is found in the loop, we set the queen to back to zero and look to move the queen to the right if there 
    is no position found to place the queen
    to the right of the previous queen we step back otherwise we step forward to the next row
    you will notice the if statements checking if numbers = 0 or Q, and the call of queen verifier, queen verifier is a 
    function that takes the positions of all queens
    and it emits '1's in all positions perpendicular horizontal and diagonal from each queen representing illegal moves
    for future queens to be placed in. This function must be called each time a new queen is placed'''

    sum_items_in_row = 0
    for item in board[test_row]:
        if item == 1:
            sum_items_in_row += 1
    if sum_items_in_row == 8:
        return queen_placer(board,test_row-1)
    '''These lines check that every item in our test_row is not currently a 1, meaning that there is both no Queen in 
    the row and no remaining position for a queen to be placed in, if that was found to be true, we must make an
    additional step back as the queens prior to this row are not positioned in a winning method'''


    for item_index in range(len(board[test_row])):
        if board[test_row][item_index] == 0:
            board[test_row][item_index] = 'Q'
            queen_emitter.queen_verifier(board)
            break
    '''The loop above places a queen in the first found zero in the row, we use this function if a queen is not in the 
    row, were as the loop above is used to move a queen that has been placed in the row'''

    if test_row != 7:
        return queen_placer(board,test_row+1)
    '''This line recurs the function for the next row if we are not in the final row'''
    return board

if __name__ == "__main__":
    chess_board = create_board()
    print(queen_placer(chess_board))