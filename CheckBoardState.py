import GUI

BOARDSIZE = 15
WIN = 5


class CheckBoardState:
    def __init__(self, board):
        self.board = board
        self.goodMoves = []

    def checkRows(self, depth):
        self.fourStones = 0
        self.threeStones = 0
        self.twoStones = 0
        self.goodMoves.clear()
        for i in range(0, BOARDSIZE):
            consecutive = 1
            for j in range(0, BOARDSIZE - 1):
                if self.board[i][j] == self.board[i][j + 1] != "_":
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    elif consecutive == 4:
                        if self.board[i][j] == "_" and self.board[i][
                            j - 4] == "_":
                            if self.board[i][j] == "white":
                                self.fourStones += 1
                            else:
                                self.fourStones -= 1
                    elif consecutive == 3:
                        if self.board[i][j + 1] == "_" and self.board[i][
                            j - 3] == "_":
                            if self.board[i][j] == "white":
                                self.threeStones += 1
                            else:
                                self.threeStones -= 1
                            self.goodMoves.append((i, j + 1, 3000))
                            self.goodMoves.append((i, j - 3, 3000))
                    elif consecutive == 2:
                        if self.board[i][j + 1] == "_" and self.board[i][
                            j - 2] == "_":
                            if self.board[i][j] == "white":
                                self.twoStones += 1
                            else:
                                self.twoStones -= 1
                    consecutive = 1
        return False

    def checkCols(self, depth):
        for j in range(0, BOARDSIZE):
            consecutive = 1
            for i in range(0, BOARDSIZE - 1):
                if self.board[i][j] == self.board[i + 1][j] != "_":
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    elif consecutive == 2:
                        if self.board[i][j] == "white":
                            self.twoStones += 1
                        else:
                            self.twoStones -= 1
                    elif consecutive == 3:
                        if self.board[i + 1][j] == "_" and self.board[i - 3][
                            j] == "_":
                            if self.board[i][j] == "white":
                                self.threeStones += 1
                            else:
                                self.threeStones -= 1
                            self.goodMoves.append((i + 1, j, 3000))
                            self.goodMoves.append((i + -3, j, 3000))
                    elif consecutive == 4:
                        if self.board[i + 1][j] == "_" and self.board[i - 4][
                            j] == "_":
                            if self.board[i][j] == "white":
                                self.fourStones += 1
                            else:
                                self.fourStones -= 1
                    consecutive = 1
        return False

    def checkDiagonal(self, depth):
        # 1 left-up corner to main diagonal(\)
        for i in range(0, BOARDSIZE):
            consecutive = 1
            for j in range(0, BOARDSIZE - i - 1):
                if self.board[j + i][j] == self.board[j + i + 1][j + 1] != "_":
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    elif consecutive == 2:
                        if self.board[j + i + 1][j + 1] == "_" and \
                                self.board[j + i - 2][j - 2] == "_":
                            if self.board[j + i][j] == "white":
                                self.twoStones += 1
                            else:
                                self.twoStones -= 1
                    elif consecutive == 3:
                        if self.board[j + i + 1][j + 1] == "_" and \
                                self.board[j + i - 3][j - 3] == "_":
                            if self.board[j + i][j] == "white":
                                self.threeStones += 1
                            else:
                                self.threeStones -= 1
                            self.goodMoves.append((j + i + 1, j + 1, 3000))
                            self.goodMoves.append((j + i - 3, j - 3, 3000))
                    elif consecutive == 4:
                        if self.board[j + i][j] == "white":
                            if self.board[j + i + 1][j + 1] == "_" or \
                                    self.board[j + i - 4][j - 4] == "_":
                                self.fourStones += 1
                            else:
                                self.fourStones -= 1
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
                    elif consecutive == 2:
                        if self.board[j + 1][j + i + 1] == "_" and \
                                self.board[j - 2][j + i - 2] == "_":
                            if self.board[j][j + i] == "white":
                                self.twoStones += 1
                            else:
                                self.twoStones -= 1
                    elif consecutive == 3:
                        # print("d1",self.board[j+1][j+i+1]," ",self.board[j][j+i],"   ",self.board[j-1][j+i-1],"   ",self.board[j-2][j+i-2],"   ",self.board[j-3][j+i-3])
                        if self.board[j + 1][j + i + 1] == "_" and \
                                self.board[j - 3][j + i - 3] == "_":
                            if self.board[j][j + i] == "white":
                                self.threeStones += 1
                            else:
                                self.threeStones -= 1
                            self.goodMoves.append((j + 1, j + i + 1, 3000))
                            self.goodMoves.append((j + -3, j + i - 3, 3000))
                    elif consecutive == 4:
                        if self.board[j + 1][j + i + 1] == "_" and \
                                self.board[j - 4][j + i - 4] == "_":
                            if self.board[j][j + i] == "white":
                                self.fourStones += 1
                            else:
                                self.fourStones -= 1
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
                    elif consecutive == 2:
                        if self.board[i - j + 2][j - 2] == "_" and \
                                self.board[i - j - 1][j + 1] == "_":
                            if self.board[i - j][j] == "white":
                                self.twoStones += 1
                            else:
                                self.twoStones -= 1
                    elif consecutive == 3:
                        if self.board[i - j + 3][j - 3] == "_" and \
                                self.board[i - j - 1][j + 1] == "_":
                            if self.board[i - j][j] == "white":
                                self.threeStones += 1
                            else:
                                self.threeStones -= 1
                            self.goodMoves.append((i - j + 3, j - 3, 3000))
                            self.goodMoves.append((i - j - 1, j + 1, 3000))
                    elif consecutive == 4:
                        if self.board[i - j + 4][j - 4] == "_" and \
                                self.board[i - j - 1][j + 1] == "_":
                            if self.board[i - j][j] == "white":
                                self.fourStones += 1
                            else:
                                self.fourStones -= 1
                    consecutive = 1

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
                    elif consecutive == 2:
                        if self.board[i + j][BOARDSIZE - 1 - j] == "_" \
                                and self.board[i + j + 3][
                            BOARDSIZE - j - 4] == "_":
                            if self.board[i + j][BOARDSIZE - 1 - j] == "white":
                                self.twoStones += 1
                            else:
                                self.twoStones -= 1
                    elif consecutive == 3:
                        if self.board[i + j][BOARDSIZE - 1 - j] == "_" \
                                and self.board[i + j + 4][
                            BOARDSIZE - j - 5] == "_":
                            if self.board[i - j][BOARDSIZE - 1 - j] == "white":
                                self.threeStones += 1
                            else:
                                self.threeStones -= 1
                            self.goodMoves.append(
                                (i + j + 1, BOARDSIZE - 2 - j, 3000))
                            self.goodMoves.append(
                                (i + j - 3, BOARDSIZE - j + 2, 3000))
                    elif consecutive == 4:
                        if self.board[i + j][BOARDSIZE - 1 - j] == "_" \
                                and self.board[i + j + 5][
                            BOARDSIZE - j - 6] == "_":
                            if self.board[i - j][BOARDSIZE - 1 - j] == "white":
                                self.fourStones += 1
                            else:
                                self.fourStones -= 1
                    consecutive = 1
        return False

    def checkWin(self, depth):
        if self.checkRows(depth) or self.checkCols(depth) or self.checkDiagonal(
                depth):
            return True
        return False

    def checkDraw(self, moveNuber):
        if moveNuber == BOARDSIZE * BOARDSIZE + 1:
            return True
        else:
            return False

    def checkBoardState(self, moveNumber, name):
        if self.checkWin(0):
            GUI.messageWin(name)
            return True
        elif self.checkDraw(moveNumber):
            GUI.messageDraw(0)
            return True
        return False

    def evaluate(self, depth):
        return (self.fourStones * (-1000) + self.threeStones * (
            -100) + self.twoStones * (-10))
