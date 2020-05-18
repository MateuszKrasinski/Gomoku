import gui

BOARDSIZE = 15
WIN = 5


class CheckBoardState:
    def __init__(self, board):
        self.board = board
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
                if self.board[i][j] == self.board[i][j + 1] != "_":
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 4:
                        if self.board[i][j] == "_" and self.board[i][j - 4] == "_":
                            if self.board[i][j] == "white":
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    elif consecutive == 3:
                        if self.board[i][j + 1] == "_" and self.board[i][j - 3] == "_":
                            if self.board[i][j] == "white":
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append((i, j + 1, 3000))
                            self.good_moves.append((i, j - 3, 3000))
                    elif consecutive == 2:
                        if self.board[i][j + 1] == "_" and self.board[i][j - 2] == "_":
                            if self.board[i][j] == "white":
                                self.two_stones += 1
                            else:
                                self.two_stones -= 1
                    consecutive = 1
        return False

    def check_cols(self):
        for j in range(0, BOARDSIZE):
            consecutive = 1
            for i in range(0, BOARDSIZE - 1):
                if self.board[i][j] == self.board[i + 1][j] != "_":
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 2:
                        if self.board[i][j] == "white":
                            self.two_stones += 1
                        else:
                            self.two_stones -= 1
                    elif consecutive == 3:
                        if self.board[i + 1][j] == "_" and self.board[i - 3][j] == "_":
                            if self.board[i][j] == "white":
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append((i + 1, j, 3000))
                            self.good_moves.append((i + -3, j, 3000))
                    elif consecutive == 4:
                        if self.board[i + 1][j] == "_" and self.board[i - 4][j] == "_":
                            if self.board[i][j] == "white":
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    consecutive = 1
        return False

    def check_diagonal(self):
        # 1 left-up corner to main diagonal(\)
        for i in range(0, BOARDSIZE):
            consecutive = 1
            for j in range(0, BOARDSIZE - i - 1):
                if self.board[j + i][j] == self.board[j + i + 1][j + 1] != "_":
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 2:
                        if self.board[j + i + 1][j + 1] == "_" and \
                                self.board[j + i - 2][j - 2] == "_":
                            if self.board[j + i][j] == "white":
                                self.two_stones += 1
                            else:
                                self.two_stones -= 1
                    elif consecutive == 3:
                        if self.board[j + i + 1][j + 1] == "_" and \
                                self.board[j + i - 3][j - 3] == "_":
                            if self.board[j + i][j] == "white":
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append((j + i + 1, j + 1, 3000))
                            self.good_moves.append((j + i - 3, j - 3, 3000))
                    elif consecutive == 4:
                        if self.board[j + i][j] == "white":
                            if self.board[j + i + 1][j + 1] == "_" or \
                                    self.board[j + i - 4][j - 4] == "_":
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    consecutive = 1
        # 2 main diagonal(\) to right-up corner
        for i in range(0, BOARDSIZE):
            consecutive = 1
            for j in range(1, BOARDSIZE - i - 1):
                if self.board[j][j + i] == self.board[j + 1][j + i + 1] != "_":
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 2:
                        if self.board[j + 1][j + i + 1] == "_" and \
                                self.board[j - 2][j + i - 2] == "_":
                            if self.board[j][j + i] == "white":
                                self.two_stones += 1
                            else:
                                self.two_stones -= 1
                    elif consecutive == 3:
                        if self.board[j + 1][j + i + 1] == "_" and \
                                self.board[j - 3][j + i - 3] == "_":
                            if self.board[j][j + i] == "white":
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append((j + 1, j + i + 1, 3000))
                            self.good_moves.append((j + -3, j + i - 3, 3000))
                    elif consecutive == 4:
                        if self.board[j + 1][j + i + 1] == "_" and \
                                self.board[j - 4][j + i - 4] == "_":
                            if self.board[j][j + i] == "white":
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    consecutive = 1
        # 3 left-down corner to main diagonal(/)
        for i in range(1, BOARDSIZE):
            consecutive = 1
            for j in range(0, i):
                if self.board[i - j][j] == self.board[i - j - 1][j + 1] != "_":
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 2:
                        if self.board[i - j + 2][j - 2] == "_" and \
                                self.board[i - j - 1][j + 1] == "_":
                            if self.board[i - j][j] == "white":
                                self.two_stones += 1
                            else:
                                self.two_stones -= 1
                    elif consecutive == 3:
                        if self.board[i - j + 3][j - 3] == "_" and \
                                self.board[i - j - 1][j + 1] == "_":
                            if self.board[i - j][j] == "white":
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append((i - j + 3, j - 3, 3000))
                            self.good_moves.append((i - j - 1, j + 1, 3000))
                    elif consecutive == 4:
                        if self.board[i - j + 4][j - 4] == "_" and \
                                self.board[i - j - 1][j + 1] == "_":
                            if self.board[i - j][j] == "white":
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    consecutive = 1
        """
        # 4 main diagonal(/) to right-up corner
        for i in range(BOARDSIZE - 1, 0, -1):
            consecutive = 1
            for j in range(0, BOARDSIZE - i):
                print(BOARDSIZE - j)
                if self.board[i + j - 1][BOARDSIZE - j - 1] == \
                        self.board[i + j][BOARDSIZE - 1 - j] != "_":
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    if consecutive == 2:
                        if self.board[i + j][BOARDSIZE - 1 - j] == "_" \
                                and self.board[i + j + 3][BOARDSIZE - j - 4] == "_":
                            if self.board[i + j][BOARDSIZE - 1 - j] == "white":
                                self.two_stones += 1
                            else:
                                self.two_stones -= 1
                    elif consecutive == 3:
                        if self.board[i + j][BOARDSIZE - 1 - j] == "_" \
                                and self.board[i + j + 4][BOARDSIZE - j - 5] == "_":
                            if self.board[i - j][BOARDSIZE - 1 - j] == "white":
                                self.three_stones += 1
                            else:
                                self.three_stones -= 1
                            self.good_moves.append(
                                (i + j + 1, BOARDSIZE - 2 - j, 3000))
                            self.good_moves.append(
                                (i + j - 3, BOARDSIZE - j + 2, 3000))
                    elif consecutive == 4:
                        if self.board[i + j][BOARDSIZE - 1 - j] == "_" \
                                and self.board[i + j + 5][BOARDSIZE - j - 6] == "_":
                            if self.board[i - j][BOARDSIZE - 1 - j] == "white":
                                self.four_stones += 1
                            else:
                                self.four_stones -= 1
                    consecutive = 1
        """
        return False

    def check_win(self):
        if self.check_rows() or self.check_cols() or self.check_diagonal():
            return True
        return False

    def check_draw(self, move_number):
        if move_number == BOARDSIZE * BOARDSIZE + 1:
            return True
        return False

    def checkBoardState(self, move_number, name):
        if self.check_win():
            gui.messageWin(name)
            return True
        if self.check_draw(move_number):
            gui.messageDraw()
            return True
        return False

    def evaluate(self):
        return (self.four_stones * (-1000) + self.three_stones * (
            -100) + self.two_stones * (-10))
