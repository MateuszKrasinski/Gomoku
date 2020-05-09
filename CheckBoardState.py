from  Globals import BOARDSIZE,WIN
import board
"""This Class checking win and draw and evaluate position"""
class CheckBoardState:
    def __init__(self,board):
        self.b=board
    def checkRows(self, depth):
        self.fourStones = 0
        self.threeStones = 0
        self.twoStones = 0
        for i in range(0, BOARDSIZE):
            consecutive = 1
            for j in range(0, BOARDSIZE - 1):
                if self.b.square[i][j].value == self.b.square[i][j + 1].value != "_":
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    elif consecutive == 4:
                        if self.b.square[i][j].value == "_" or self.b.square[i][j - 4].value == "_":
                            if self.b.square[i][j].value == "white":
                                self.fourStones += 1
                            else:
                                self.fourStones -= 1
                    elif consecutive == 3:
                        if self.b.square[i][j + 1].value == "_" and self.b.square[i][j - 3].value == "_":
                            if self.b.square[i][j].value == "white":
                                self.threeStones += 1
                            else:
                                self.threeStones -= 1
                    elif consecutive == 2:
                        if self.b.square[i][j + 1].value == "_" and self.b.square[i][j - 2].value == "_":
                            if self.b.square[i][j].value == "white":
                                self.twoStones += 1
                            else:
                                self.twoStones -= 1
                    consecutive = 1
        return False


    def checkCols(self, depth):
        for j in range(0, BOARDSIZE):
            consecutive = 1
            for i in range(0, BOARDSIZE - 1):
                if self.b.square[i][j].value == self.b.square[i + 1][j].value != "_":
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    elif consecutive == 2:
                        if self.b.square[i][j].value == "white":
                            self.twoStones += 1
                        else:
                            self.twoStones -= 1
                    elif consecutive == 3:
                        if self.b.square[i + 1][j].value == "_" and self.b.square[i - 3][j].value == "_":
                            if self.b.square[i][j].value == "white":
                                self.threeStones += 1
                            else:
                                self.threeStones -= 1
                    elif consecutive == 4:
                        if self.b.square[i + 1][j].value == "_" or self.b.square[i - 4][j].value == "_":
                            if self.b.square[i][j].value == "white":
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
                if self.b.square[j + i][j].value == self.b.square[j + i + 1][j + 1].value != "_":
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    elif consecutive == 2:
                        if self.b.square[j + i + 1][j + 1].value == "_" and self.b.square[j + i - 2][j - 2].value == "_":
                            if self.b.square[j + i][j].value == "white":
                                self.twoStones += 1
                            else:
                                self.twoStones -= 1
                    elif consecutive == 3:
                        if self.b.square[j + i + 1][j + 1].value == "_" and self.b.square[j + i - 3][j - 3].value == "_":
                            if self.b.square[j + i][j].value == "white":
                                self.threeStones += 1
                            else:
                                self.threeStones -= 1
                    elif consecutive == 4:
                        if self.b.square[j + i][j].value == "white":
                            if self.b.square[j + i + 1][j + 1].value == "_" or self.b.square[j + i - 4][j - 4].value == "_":
                                self.fourStones += 1
                            else:
                                self.fourStones -= 1
                    consecutive = 1
        # 2 main diagonal(\) to right-up corner
        for i in range(0, BOARDSIZE):
            consecutive = 1
            for j in range(1, BOARDSIZE - i - 1):
                if self.b.square[j][j + i].value == self.b.square[j + 1][j + i + 1].value != "_":
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    elif consecutive == 2:
                        if self.b.square[j + 1][j + i + 1].value == "_" and self.b.square[j - 2][j + i - 2].value == "_":
                            if self.b.square[j][j + i].value == "white":
                                self.twoStones += 1
                            else:
                                self.twoStones -= 1
                    elif consecutive == 3:
                        # print("d1",self.b.square[j+1][j+i+1].value," ",self.b.square[j][j+i].value,"   ",self.b.square[j-1][j+i-1].value,"   ",self.b.square[j-2][j+i-2].value,"   ",self.b.square[j-3][j+i-3].value)
                        if self.b.square[j + 1][j + i + 1].value == "_" and self.b.square[j - 3][j + i - 3].value == "_":
                            if self.b.square[j][j + i].value == "white":
                                self.threeStones += 1
                            else:
                                self.threeStones -= 1
                    elif consecutive == 4:
                        if self.b.square[j + 1][j + i + 1].value == "_" or self.b.square[j - 4][j + i - 4].value == "_":
                            if self.b.square[j][j + i].value == "white":
                                self.fourStones += 1
                            else:
                                self.fourStones -= 1
                    consecutive = 1
        # 3 left-down corner to main diagonal(/)
        for i in range(1, BOARDSIZE):
            consecutive = 1
            for j in range(0, i):
                if self.b.square[i - j][j].value == self.b.square[i - j - 1][j + 1].value != "_":
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    elif consecutive == 2:
                        if self.b.square[i - j + 2][j - 2].value == "_" and self.b.square[i - j - 1][j + 1].value == "_":
                            if self.b.square[i - j][j].value == "white":
                                self.twoStones += 1
                            else:
                                self.twoStones -= 1
                    elif consecutive == 3:
                        if self.b.square[i - j + 3][j - 3].value == "_" and self.b.square[i - j - 1][j + 1].value == "_":
                            if self.b.square[i - j][j].value == "white":
                                self.threeStones += 1
                            else:
                                self.threeStones -= 1
                    elif consecutive == 4:
                        if self.b.square[i - j + 4][j - 4].value == "_" or self.b.square[i - j - 1][j + 1].value == "_":
                            if self.b.square[i - j][j].value == "white":
                                self.fourStones += 1
                            else:
                                self.fourStones -= 1
                    consecutive = 1

        # 4 main diagonal(/) to right-up corner
        for i in range(BOARDSIZE - 5, 0, -1):
            consecutive = 1
            for j in range(0, BOARDSIZE - i - 1):
                if self.b.square[i + j][BOARDSIZE - 1 - j].value == \
                        self.b.square[i + j + 1][BOARDSIZE - 2 - j].value != "_":
                    consecutive += 1
                else:
                    if consecutive == WIN:
                        return True
                    elif consecutive == 2:
                        if self.b.square[i + j + 1][BOARDSIZE - 2 - j].value == "_" \
                                and self.b.square[i + j - 2][BOARDSIZE - j + 1].value == "_":
                            if self.b.square[i + j][BOARDSIZE - 1 - j].value == "white":
                                self.twoStones += 1
                            else:
                                self.twoStones -= 1
                    elif consecutive == 3:
                        if self.b.square[i + j + 1][BOARDSIZE - 2 - j].value == "_" \
                                and self.b.square[i + j - 3][BOARDSIZE - j + 2].value == "_":
                            if self.b.square[i - j][BOARDSIZE - 1 - j].value == "white":
                                self.threeStones += 1
                            else:
                                self.threeStones -= 1
                    elif consecutive == 4:
                        if self.b.square[i + j + 1][BOARDSIZE - 2 - j].value == "_" \
                                or self.b.square[i + j - 4][BOARDSIZE - j + 3].value == "_":
                            if self.b.square[i - j][BOARDSIZE - 1 - j].value == "white":
                                self.fourStones += 1
                            else:
                                self.fourStones -= 1
                    consecutive = 1
        return False
    def checkWin(self, depth):
        if self.checkRows(depth) or self.checkCols(depth) or self.checkDiagonal(depth):
            return True
        return False

    def checkDraw(self,moveNuber):
        if moveNuber == BOARDSIZE * BOARDSIZE + 1:
            return True
        else:
            return False
    def checkBoardState(self,moveNumber):
        if self.checkWin(0):
            board.messageWin()
            return True
        elif self.checkDraw(moveNumber):
            board.messageDraw(0)
            return True
        return False
    def evaluate(self,depth):
        return (self.fourStones * (-1000) + self.threeStones * (-100) + self.twoStones * (-10))