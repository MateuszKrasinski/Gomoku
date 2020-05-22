"""Module tests check_board_state module"""
import unittest

import check_board_state

EMPTY = "_"
BOARD_SIZE = 15


class TestCheckBoardStateClass(unittest.TestCase):
    """Class testing CheckBoardStateClass."""
    def setUp(self):
        """Creating clear board 15x15 to set on this board situations to test."""
        self.board = [[EMPTY for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

    def test_check_rows(self):
        """Checking if method check_rows() returns True if put five consecutive stones in row."""
        self.setUp()
        self.board[5][1] = "white"
        self.board[5][2] = "white"
        self.board[5][3] = "white"
        self.board[5][4] = "white"
        self.board[5][5] = "white"
        result = check_board_state.CheckBoardState(self.board).check_rows()
        self.assertTrue(result, True)

    def test_check_cols(self):
        """Checking if method check_cols() returns True if put five consecutive stones in col."""
        self.setUp()
        self.board[1][5] = "white"
        self.board[2][5] = "white"
        self.board[3][5] = "white"
        self.board[4][5] = "white"
        self.board[5][5] = "white"
        result = check_board_state.CheckBoardState(self.board).check_cols()
        self.assertTrue(result, True)

    def test_check_diagonal(self):
        """Checking if method check_diagonal() returns True if put five consecutive stones."""
        self.setUp()
        self.board[0][0] = "white"
        self.board[1][1] = "white"
        self.board[2][2] = "white"
        self.board[3][3] = "white"
        self.board[4][4] = "white"
        result = check_board_state.CheckBoardState(self.board).check_diagonal()
        self.assertTrue(result)

    def test_check_win(self):
        """Checking if method check_win() returns True if put five consecutive stones."""
        self.setUp()
        self.board = [[EMPTY for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
        self.board[1][13] = "white"
        self.board[2][12] = "white"
        self.board[3][11] = "white"
        self.board[4][10] = "white"
        self.board[5][9] = "white"
        result = check_board_state.CheckBoardState(self.board).check_win()
        self.assertTrue(result)

    def test_check_draw(self):
        """Checking check_draw() returns True if fill board with one color (only 5 stones wins)."""
        self.setUp()
        self.board = [["white" for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
        result = check_board_state.CheckBoardState(self.board).check_draw()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
