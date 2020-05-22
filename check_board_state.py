import gui

BOARDSIZE = 15
WIN = 5
EMPTY = "_"
WHITE = "white"
GOOD_MOVE = 3000


class CheckBoardState:
    def __init__(self, board):
        self.game_board = board
        self.good_moves = []
        self.four_stones = 0
        self.three_stones = 0
        self.two_stones = 0

    def check_rows(self):
        self.four_stones = 0
        self.three_stones = 0
        self.two_stones = 0
        self.good_moves.clear()
        for i in range(0, BOARDSIZE):
            consecutive = 1
            for j in range(0, BOARDSIZE - 1):
                if self.game_board[i][j] == self.game_board[i][j + 1] != EMPTY:
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 4:
                        if self.game_board[i][j + 1] == EMPTY and self.game_board[i][
                            j - 4] == EMPTY:
                            if self.game_board[i][j] == WHITE:
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    elif consecutive == 3:
                        if self.game_board[i][j + 1] == EMPTY and self.game_board[i][
                            j - 3] == EMPTY:
                            if self.game_board[i][j] == WHITE:
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append((i, j + 1, GOOD_MOVE))
                            self.good_moves.append((i, j - 3, GOOD_MOVE))
                    elif consecutive == 2:
                        if self.game_board[i][j + 1] == EMPTY and self.game_board[i][
                            j - 2] == EMPTY:
                            if self.game_board[i][j] == WHITE:
                                self.two_stones += 1
                            else:
                                self.two_stones -= 1
                    consecutive = 1
        return False

    def check_cols(self):
        for j in range(0, BOARDSIZE):
            consecutive = 1
            for i in range(0, BOARDSIZE - 1):
                if self.game_board[i][j] == self.game_board[i + 1][j] != EMPTY:
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 2:
                        if self.game_board[i][j] == WHITE:
                            self.two_stones += 1
                        else:
                            self.two_stones -= 1
                    elif consecutive == 3:
                        if self.game_board[i + 1][j] == EMPTY and self.game_board[i - 3][
                            j] == EMPTY:
                            if self.game_board[i][j] == WHITE:
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append((i + 1, j, GOOD_MOVE))
                            self.good_moves.append((i + -3, j, GOOD_MOVE))
                    elif consecutive == 4:
                        if self.game_board[i + 1][j] == EMPTY and self.game_board[i - 4][
                            j] == EMPTY:
                            if self.game_board[i][j] == WHITE:
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    consecutive = 1
        return False

    def check_diagonal(self):
        # 1 left-up corner to main diagonal(\)
        for i in range(1, BOARDSIZE):
            consecutive = 1
            for j in range(0, BOARDSIZE - i - 1):
                if self.game_board[j + i][j] == self.game_board[j + i + 1][j + 1] != EMPTY:
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 2:
                        if self.game_board[j + i + 1][j + 1] == EMPTY and \
                                self.game_board[j + i - 2][j - 2] == EMPTY:
                            if self.game_board[j + i][j] == WHITE:
                                self.two_stones += 1
                            else:
                                self.two_stones -= 1
                    elif consecutive == 3:
                        if self.game_board[j + i + 1][j + 1] == EMPTY and \
                                self.game_board[j + i - 3][j - 3] == EMPTY:
                            if self.game_board[j + i][j] == WHITE:
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append((j + i + 1, j + 1, GOOD_MOVE))
                            self.good_moves.append((j + i - 3, j - 3, GOOD_MOVE))
                    elif consecutive == 4:
                        if self.game_board[j + i][j] == WHITE:
                            if self.game_board[j + i + 1][j + 1] == EMPTY and \
                                    self.game_board[j + i - 4][j - 4] == EMPTY:
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    consecutive = 1
        # 2 main diagonal(\) to right-up corner
        for i in range(0, BOARDSIZE):
            consecutive = 1
            for j in range(0, BOARDSIZE - i - 1):
                if self.game_board[j][j + i] == self.game_board[j + 1][j + i + 1] != EMPTY:
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 2:
                        if self.game_board[j + 1][j + i + 1] == EMPTY and \
                                self.game_board[j - 2][j + i - 2] == EMPTY:
                            if self.game_board[j][j + i] == WHITE:
                                self.two_stones += 1
                            else:
                                self.two_stones -= 1
                    elif consecutive == 3:
                        if self.game_board[j + 1][j + i + 1] == EMPTY and \
                                self.game_board[j - 3][j + i - 3] == EMPTY:
                            if self.game_board[j][j + i] == WHITE:
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append((j + 1, j + i + 1, GOOD_MOVE))
                            self.good_moves.append((j + -3, j + i - 3, GOOD_MOVE))
                    elif consecutive == 4:
                        if self.game_board[j + 1][j + i + 1] == EMPTY and \
                                self.game_board[j - 4][j + i - 4] == EMPTY:
                            if self.game_board[j][j + i] == WHITE:
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    consecutive = 1
        # 3 left-down corner to main diagonal(/)
        for i in range(0, BOARDSIZE):
            consecutive = 1
            for j in range(0, i):
                if self.game_board[i - j][j] == self.game_board[i - j - 1][j + 1] != EMPTY:
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 2 and i - j + 2 <= BOARDSIZE - 1:
                        if self.game_board[i - j + 2][j - 2] == EMPTY and \
                                self.game_board[i - j - 1][j + 1] == EMPTY:
                            if self.game_board[i - j][j] == WHITE:
                                self.two_stones += 1
                            else:
                                self.two_stones -= 1
                    elif consecutive == 3 and i - j + 3 <= BOARDSIZE - 1:
                        if self.game_board[i - j + 3][j - 3] == EMPTY and \
                                self.game_board[i - j - 1][j + 1] == EMPTY:
                            if self.game_board[i - j][j] == WHITE:
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append((i - j + 3, j - 3, GOOD_MOVE))
                            self.good_moves.append((i - j - 1, j + 1, GOOD_MOVE))
                    elif consecutive == 4 and i - j + 4 <= BOARDSIZE - 1:
                        if self.game_board[i - j + 4][j - 4] == EMPTY and \
                                self.game_board[i - j - 1][j + 1] == EMPTY:
                            if self.game_board[i - j][j] == WHITE:
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    consecutive = 1

        # 4 main diagonal(/) to right-up corner
        for i in range(0, BOARDSIZE):
            consecutive = 1
            for j in range(0, BOARDSIZE - i - 1):
                if self.game_board[i + j + 1][BOARDSIZE - 1 - j - 1] == \
                        self.game_board[i + j][BOARDSIZE - 1 - j] != EMPTY:
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 2 and BOARDSIZE - 1 - j + 2 <= 14:
                        if self.game_board[i + j + 1][BOARDSIZE - 1 - j - 1] == EMPTY \
                                and self.game_board[i + j - 2][BOARDSIZE - 1 - j + 2] == EMPTY:
                            if self.game_board[i + j][BOARDSIZE - 1 - j] == WHITE:
                                self.two_stones += 1
                            else:
                                self.two_stones -= 1
                    elif consecutive == 3 and BOARDSIZE - 1 - j + 3 <= 14:
                        if self.game_board[i + j + 1][BOARDSIZE - 1 - j - 1] == EMPTY \
                                and self.game_board[i + j - 3][BOARDSIZE - 1 - j + 3] == EMPTY:
                            if self.game_board[i + j][BOARDSIZE - 1 - j] == WHITE:
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append(
                                (i + j + 1, BOARDSIZE - 1 - j - 1, GOOD_MOVE))
                            self.good_moves.append(
                                (i + j - 3, BOARDSIZE - j + 2, GOOD_MOVE))
                    elif consecutive == 4 and BOARDSIZE - 1 - j + 3 <= 14:
                        if self.game_board[i + j][BOARDSIZE - 1 - j] == EMPTY \
                                and self.game_board[i + j - 4][BOARDSIZE - 1 - j + 4] == EMPTY:
                            if self.game_board[i + j][BOARDSIZE - 1 - j] == WHITE:
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    consecutive = 1

        return False

    def check_win(self):
        if self.check_rows() or self.check_cols() or self.check_diagonal():
            return True
        return False

    def check_draw(self, move_number=0):
        for i in range(15):
            for j in range(15):
                if self.game_board[i][j] == EMPTY:
                    return False
        return True

    def check_board_state(self, name):
        if self.check_win():
            gui.message_win(name)
            return True
        if self.check_draw():
            gui.message_draw()
            return True
        return False

    def evaluate(self):
        return (self.four_stones * (-1000) + self.three_stones * (
            -100) + self.two_stones * (-10))
