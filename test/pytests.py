import pytest
import queen_emitter
chess_board = []
for _ in range(8):
  chess_board.append([0] * 8)
test_one_board = chess_board
test_one_board[0][0] = 'Q'
test_one_solution = [["Q",1,1,1,1,1,1,1],[1,1,0,0,0,0,0,0],[1,0,1,0,0,0,0,0],[1,0,0,1,0,0,0,0],[1,0,0,0,1,0,0,0],[1,0,0,0,0,1,0,0],[1,0,0,0,0,0,1,0],[1,0,0,0,0,0,0,1]]
def test_queen_emitter():
    assert queen_emitter.queen_emitter(test_one_board,0,0) == test_one_solution