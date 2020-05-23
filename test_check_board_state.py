"""Module tests check_board_state module"""
import unittest

import check_board_state
import globals


class TestCheckBoardStateClass(unittest.TestCase):
    """Class testing CheckBoardStateClass."""

    def setUp(self):
        """Creating clear board 15x15 to set on this board situations to test."""
        self.board = [[globals.EMPTY for i in range(globals.BOARD_SIZE)] for j in range(
            globals.BOARD_SIZE)]

    def test_check_rows(self):
        """Checking if method check_rows() returns True if put five consecutive stones in row."""
        self.board[5][1] = globals.BLACK
        self.board[5][2] = globals.BLACK
        self.board[5][3] = globals.BLACK
        self.board[5][4] = globals.BLACK
        self.board[5][5] = globals.BLACK
        result = check_board_state.CheckBoardState(self.board).check_rows()
        self.assertTrue(result, True)

    def test_check_cols(self):
        """Checking if method check_cols() returns True if put five consecutive stones in col."""
        self.board[1][5] = globals.WHITE
        self.board[2][5] = globals.WHITE
        self.board[3][5] = globals.WHITE
        self.board[4][5] = globals.WHITE
        self.board[5][5] = globals.WHITE
        result = check_board_state.CheckBoardState(self.board).check_cols()
        self.assertTrue(result, True)

    def test_check_diagonal(self):
        """Checking if method check_diagonal() returns True if put five consecutive stones."""
        self.board[0][0] = globals.WHITE
        self.board[1][1] = globals.WHITE
        self.board[2][2] = globals.WHITE
        self.board[3][3] = globals.WHITE
        self.board[4][4] = globals.WHITE
        result = check_board_state.CheckBoardState(self.board).check_diagonal()
        self.assertTrue(result)

    def test_check_win(self):
        """Checking if method check_win() returns True if put five consecutive stones."""
        self.board[1][13] = globals.WHITE
        self.board[2][12] = globals.WHITE
        self.board[3][11] = globals.WHITE
        self.board[4][10] = globals.WHITE
        self.board[5][9] = globals.WHITE
        result = check_board_state.CheckBoardState(self.board).check_win()
        self.assertTrue(result)

    def test_check_draw(self):
        """Checking check_draw() returns True if fill board with one color (only 5 stones wins)."""
        self.board = [[globals.WHITE for i in range(globals.BOARD_SIZE)] for j in range(
            globals.BOARD_SIZE)]
        result = check_board_state.CheckBoardState(self.board).check_draw()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
