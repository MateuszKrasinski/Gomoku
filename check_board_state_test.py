"""Module tests check_board_state module"""
import unittest

import check_board_state
import constants


class TestCheckBoardStateClass(unittest.TestCase):
    """Class testing CheckBoardStateClass."""

    def setUp(self):
        """Creating clear board 15x15 to set on this board situations to test."""
        self.board = check_board_state.create_board()

    def test_check_rows(self):
        """Checking if method check_rows() returns True if put five consecutive stones in row."""
        self.board[5][1] = constants.BLACK
        self.board[5][2] = constants.BLACK
        self.board[5][3] = constants.BLACK
        self.board[5][4] = constants.BLACK
        self.board[5][5] = constants.BLACK
        result = check_board_state.CheckBoardState(self.board).check_rows()
        self.assertTrue(result, True)

    def test_check_cols(self):
        """Checking if method check_cols() returns True if put five consecutive stones in col."""
        self.board[1][5] = constants.WHITE
        self.board[2][5] = constants.WHITE
        self.board[3][5] = constants.WHITE
        self.board[4][5] = constants.WHITE
        self.board[5][5] = constants.WHITE
        result = check_board_state.CheckBoardState(self.board).check_cols()
        self.assertTrue(result, True)

    def test_check_diagonal(self):
        """Checking if method check_diagonal() returns True if put five consecutive stones."""
        self.board[0][0] = constants.WHITE
        self.board[1][1] = constants.WHITE
        self.board[2][2] = constants.WHITE
        self.board[3][3] = constants.WHITE
        self.board[4][4] = constants.WHITE
        result = check_board_state.CheckBoardState(self.board).check_diagonal()
        self.assertTrue(result)

    def test_check_win(self):
        """Checking if method check_win() returns True if put five consecutive stones."""
        self.board[1][13] = constants.WHITE
        self.board[2][12] = constants.WHITE
        self.board[3][11] = constants.WHITE
        self.board[4][10] = constants.WHITE
        self.board[5][9] = constants.WHITE
        result = check_board_state.CheckBoardState(self.board).check_win()
        self.assertTrue(result)

    def test_check_draw(self):
        """Checking check_draw() returns True if fill board with one color (only 5 stones wins)."""
        self.board = [[constants.WHITE for i in range(constants.BOARD_SIZE)] for j in range(
            constants.BOARD_SIZE)]
        result = check_board_state.CheckBoardState(self.board).check_draw()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
