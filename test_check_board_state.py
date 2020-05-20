import unittest
import check_board_state

EMPTY = "_"
BOARDSIZE = 15
board = [[EMPTY for i in range(BOARDSIZE)] for j in range(BOARDSIZE)]


class TestCheckBoardStateClass(unittest.TestCase):
    def test_check_rows(self):
        board = [[EMPTY for i in range(BOARDSIZE)] for j in range(BOARDSIZE)]
        board[5][1] = "white"
        board[5][2] = "white"
        board[5][3] = "white"
        board[5][4] = "white"
        board[5][5] = "white"
        result = check_board_state.CheckBoardState(board).check_rows()
        self.assertTrue(result, True)

    def test_check_cols(self):
        board = [[EMPTY for i in range(BOARDSIZE)] for j in range(BOARDSIZE)]
        board[1][5] = "white"
        board[2][5] = "white"
        board[3][5] = "white"
        board[4][5] = "white"
        board[5][5] = "white"
        result = check_board_state.CheckBoardState(board).check_cols()
        self.assertTrue(result, True)

    def test_check_diagonal(self):
        board = [[EMPTY for i in range(BOARDSIZE)] for j in range(BOARDSIZE)]
        board[0][0] = "white"
        board[1][1] = "white"
        board[2][2] = "white"
        board[3][3] = "white"
        board[4][4] = "white"
        result = check_board_state.CheckBoardState(board).check_diagonal()
        self.assertTrue(result)
    def test_check_win(self):
        board = [[EMPTY for i in range(BOARDSIZE)] for j in range(BOARDSIZE)]
        board[0][0] = "white"
        board[1][1] = "white"
        board[2][2] = "white"
        board[3][3] = "white"
        board[4][4] = "white"
        result = check_board_state.CheckBoardState(board).check_win()
        self.assertTrue(result)

    def test_five_in_diagonal_win(self):
        board = [["white" for i in range(BOARDSIZE)] for j in range(BOARDSIZE)]
        result=check_board_state.CheckBoardState(board).check_draw()
        self.assertTrue(result)



if __name__ == '__main__':
    unittest.main()
