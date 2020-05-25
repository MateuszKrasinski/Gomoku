"""Module contains class CheckBoardState which allows to find end of the game."""
import gui
import constants
WIN = 5
GOOD_MOVE = 3000


class CheckBoardState:
    """Class has all attributes to find end of the game and count consecutive stones.

    During checking if on board are 5 consecutive stones (WIN) counting number of 2,3,4 stones
    in one line. Good moves list contains all threatening square when 3 stones are consecutive
    """

    def __init__(self, board):
        self.game_board = board
        self.good_moves = []
        self.four_stones = 0
        self.three_stones = 0
        self.two_stones = 0

    def check_rows(self):
        """Checking if there is 5 stones in row return True else evaluate position."""
        self.four_stones = 0
        self.three_stones = 0
        self.two_stones = 0
        self.good_moves.clear()
        for i in range(0, constants.BOARD_SIZE):
            consecutive = 1
            for j in range(0, constants.BOARD_SIZE - 1):
                if self.game_board[i][j] == self.game_board[i][j + 1] != constants.EMPTY:
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 4:
                        if self.game_board[i][j + 1] == constants.EMPTY and self.game_board[i][
                                j - 4] == constants.EMPTY:
                            if self.game_board[i][j] == constants.WHITE:
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    elif consecutive == 3:
                        if self.game_board[i][j + 1] == constants.EMPTY and self.game_board[i][
                                j - 3] == constants.EMPTY:
                            if self.game_board[i][j] == constants.WHITE:
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append((i, j + 1, GOOD_MOVE))
                            self.good_moves.append((i, j - 3, GOOD_MOVE))
                    elif consecutive == 2:
                        if self.game_board[i][j + 1] == constants.EMPTY and self.game_board[i][
                                j - 2] == constants.EMPTY:
                            if self.game_board[i][j] == constants.WHITE:
                                self.two_stones += 1
                            else:
                                self.two_stones -= 1
                    consecutive = 1
        return False

    def check_cols(self):
        """Checking if there is 5 stones in cols return True else evaluate position."""
        for j in range(0, constants.BOARD_SIZE):
            consecutive = 1
            for i in range(0, constants.BOARD_SIZE - 1):
                if self.game_board[i][j] == self.game_board[i + 1][j] != constants.EMPTY:
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 2:
                        if self.game_board[i][j] == constants.WHITE:
                            self.two_stones += 1
                        else:
                            self.two_stones -= 1
                    elif consecutive == 3:
                        if self.game_board[i + 1][j] == constants.EMPTY and self.game_board[i - 3][
                                j] == constants.EMPTY:
                            if self.game_board[i][j] == constants.WHITE:
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append((i + 1, j, GOOD_MOVE))
                            self.good_moves.append((i + -3, j, GOOD_MOVE))
                    elif consecutive == 4:
                        if self.game_board[i + 1][j] == constants.EMPTY and self.game_board[i - 4][
                                j] == constants.EMPTY:
                            if self.game_board[i][j] == constants.WHITE:
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    consecutive = 1
        return False

    def check_diagonal(self):
        """Checking if there is 5 stones in diagonal return True else evaluate position."""
        # 1 left-up corner to main diagonal(\)
        for i in range(1, constants.BOARD_SIZE):
            consecutive = 1
            for j in range(0, constants.BOARD_SIZE - i - 1):
                if self.game_board[j + i][j] == self.game_board[j + i + 1][j + 1] != constants.EMPTY:
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 2:
                        if self.game_board[j + i + 1][j + 1] == constants.EMPTY and \
                                self.game_board[j + i - 2][j - 2] == constants.EMPTY:
                            if self.game_board[j + i][j] == constants.WHITE:
                                self.two_stones += 1
                            else:
                                self.two_stones -= 1
                    elif consecutive == 3:
                        if self.game_board[j + i + 1][j + 1] == constants.EMPTY and \
                                self.game_board[j + i - 3][j - 3] == constants.EMPTY:
                            if self.game_board[j + i][j] == constants.WHITE:
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append((j + i + 1, j + 1, GOOD_MOVE))
                            self.good_moves.append((j + i - 3, j - 3, GOOD_MOVE))
                    elif consecutive == 4:
                        if self.game_board[j + i][j] == constants.WHITE:
                            if self.game_board[j + i + 1][j + 1] == constants.EMPTY and \
                                    self.game_board[j + i - 4][j - 4] == constants.EMPTY:
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    consecutive = 1
        # 2 main diagonal(\) to right-up corner
        for i in range(0, constants.BOARD_SIZE):
            consecutive = 1
            for j in range(0, constants.BOARD_SIZE - i - 1):
                if self.game_board[j][j + i] == self.game_board[j + 1][j + i + 1] != constants.EMPTY:
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 2:
                        if self.game_board[j + 1][j + i + 1] == constants.EMPTY and \
                                self.game_board[j - 2][j + i - 2] == constants.EMPTY:
                            if self.game_board[j][j + i] == constants.WHITE:
                                self.two_stones += 1
                            else:
                                self.two_stones -= 1
                    elif consecutive == 3:
                        if self.game_board[j + 1][j + i + 1] == constants.EMPTY and \
                                self.game_board[j - 3][j + i - 3] == constants.EMPTY:
                            if self.game_board[j][j + i] == constants.WHITE:
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append((j + 1, j + i + 1, GOOD_MOVE))
                            self.good_moves.append((j + -3, j + i - 3, GOOD_MOVE))
                    elif consecutive == 4:
                        if self.game_board[j + 1][j + i + 1] == constants.EMPTY and \
                                self.game_board[j - 4][j + i - 4] == constants.EMPTY:
                            if self.game_board[j][j + i] == constants.WHITE:
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    consecutive = 1
        # 3 left-down corner to main diagonal(/)
        for i in range(0, constants.BOARD_SIZE):
            consecutive = 1
            for j in range(0, i):
                if self.game_board[i - j][j] == self.game_board[i - j - 1][j + 1] != constants.EMPTY:
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 2 and i - j + 2 <= constants.BOARD_SIZE - 1:
                        if self.game_board[i - j + 2][j - 2] == constants.EMPTY and \
                                self.game_board[i - j - 1][j + 1] == constants.EMPTY:
                            if self.game_board[i - j][j] == constants.WHITE:
                                self.two_stones += 1
                            else:
                                self.two_stones -= 1
                    elif consecutive == 3 and i - j + 3 <= constants.BOARD_SIZE - 1:
                        if self.game_board[i - j + 3][j - 3] == constants.EMPTY and \
                                self.game_board[i - j - 1][j + 1] == constants.EMPTY:
                            if self.game_board[i - j][j] == constants.WHITE:
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append((i - j + 3, j - 3, GOOD_MOVE))
                            self.good_moves.append((i - j - 1, j + 1, GOOD_MOVE))
                    elif consecutive == 4 and i - j + 4 <= constants.BOARD_SIZE - 1:
                        if self.game_board[i - j + 4][j - 4] == constants.EMPTY and \
                                self.game_board[i - j - 1][j + 1] == constants.EMPTY:
                            if self.game_board[i - j][j] == constants.WHITE:
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    consecutive = 1

        # 4 main diagonal(/) to right-up corner
        for i in range(0, constants.BOARD_SIZE):
            consecutive = 1
            for j in range(0, constants.BOARD_SIZE - i - 1):
                if self.game_board[i + j + 1][constants.BOARD_SIZE - 1 - j - 1] == \
                        self.game_board[i + j][constants.BOARD_SIZE - 1 - j] != constants.EMPTY:
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 2 and constants.BOARD_SIZE - 1 - j + 2 <= 14:
                        if self.game_board[i + j + 1][constants.BOARD_SIZE - 1 - j - 1] == constants.EMPTY \
                                and self.game_board[i + j - 2][constants.BOARD_SIZE - 1 - j + 2] == constants.EMPTY:
                            if self.game_board[i + j][constants.BOARD_SIZE - 1 - j] == constants.WHITE:
                                self.two_stones += 1
                            else:
                                self.two_stones -= 1
                    elif consecutive == 3 and constants.BOARD_SIZE - 1 - j + 3 <= 14:
                        if self.game_board[i + j + 1][constants.BOARD_SIZE - 1 - j - 1] == constants.EMPTY \
                                and self.game_board[i + j - 3][constants.BOARD_SIZE - 1 - j + 3] == constants.EMPTY:
                            if self.game_board[i + j][constants.BOARD_SIZE - 1 - j] == constants.WHITE:
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append(
                                (i + j + 1, constants.BOARD_SIZE - 1 - j - 1, GOOD_MOVE))
                            self.good_moves.append(
                                (i + j - 3, constants.BOARD_SIZE - j + 2, GOOD_MOVE))
                    elif consecutive == 4 and constants.BOARD_SIZE - 1 - j + 3 <= 14:
                        if self.game_board[i + j][constants.BOARD_SIZE - 1 - j] == constants.EMPTY \
                                and self.game_board[i + j - 4][constants.BOARD_SIZE - 1 - j + 4] == constants.EMPTY:
                            if self.game_board[i + j][constants.BOARD_SIZE - 1 - j] == constants.WHITE:
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    consecutive = 1

        return False

    def check_win(self):
        """Method returns True if found winning combination."""
        if self.check_rows() or self.check_cols() or self.check_diagonal():
            return True
        return False

    def check_draw(self):
        """Method returns True if found drawing combination."""
        for i in range(15):
            for j in range(15):
                if self.game_board[i][j] == constants.EMPTY:
                    return False
        return True

    def check_board_state(self, name):
        """Return true if finds end of game."""
        if self.check_win():
            gui.message_win(name)
            return True
        if self.check_draw():
            gui.message_draw()
            return True
        return False

    def evaluate(self):
        """Evaluate position basing on number of consecutive stones."""
        return (self.four_stones * (-1000) + self.three_stones * (
            -100) + self.two_stones * (-10))
