import pygame, sys, time, Globals, math
import board
from pygame import mixer
import random

pygame.init()
pygame.display.set_caption('Gomoku')


def message(what, x, y):
    font = pygame.font.Font("freesansbold.ttf", 72)
    text = font.render(what, True, (0, 128, 0))
    Globals.screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))


class Game:
    def __init__(self):
        self.run = True
        self.moveNumber = 1
        self.board = board.Board()
        self.onMove = "white"
        self.twoWhiteInRow = 0
        self.twoWhiteInCol = 0
        self.twoWhiteInDiagonal = 0
        self.twoBlackInDiagonal = 0
        self.twoBlackInRow = 0
        self.twoBlackInCol = 0
        self.threeWhiteInRow = 0
        self.threeWhiteInCol = 0
        self.threeWhiteInDiagonal = 0
        self.threeBlackInDiagonal = 0
        self.threeBlackInRow = 0
        self.threeBlackInCol = 0
        self.fourBlackInCol = 0
        self.fourBlackInRow = 0
        self.fourBlackInDiagonal = 0
        self.fourWhiteInDiagonal = 0
        self.fourWhiteInCol = 0
        self.fourWhiteInRow = 0
        self.importantMoves = set()

    def checkRows(self):
        self.fourBlackInRow = 0
        self.fourWhiteInRow = 0
        self.threeWhiteInRow = 0
        self.threeBlackInRow = 0
        self.twoWhiteInRow = 0
        self.twoBlackInRow = 0
        rowScore = 1
        for i in range(0, Globals.BOARDSIZE):
            rowScore = 1
            for j in range(1, Globals.BOARDSIZE):
                if self.board.square[i][j].value == self.board.square[i][j - 1].value != "_":
                    rowScore = rowScore + 1
                    if rowScore == Globals.WIN:
                        return True
                    if rowScore == 2:
                        if self.board.square[i][j + 1].value == "_" and self.board.square[i][j - 2].value == "_":
                            if self.board.square[i][j].value == "white":
                                self.twoWhiteInRow += 1
                            else:
                                self.twoBlackInRow += 1
                    if rowScore == 3:
                        if self.board.square[i][j + 1].value == "_" and self.board.square[i][j - 3].value == "_":
                            if self.board.square[i][j].value == "white":
                                self.threeWhiteInRow += 1
                            else:
                                self.threeBlackInRow += 1
                    if rowScore == 4:
                        if self.board.square[i][j + 1].value == "_" or self.board.square[i][j - 4].value == "_":
                            if self.board.square[i][j].value == "white":
                                self.fourWhiteInRow += 1
                            else:
                                self.fourBlackInRow += 1
                            self.importantMoves.add((i, j + 1, 690000))
                            self.importantMoves.add((i, j - 3, 690000))
                else:
                    rowScore = 1
                    """
        print()
        print("Number of two black in rows:", self.twoBlackInRow)
        print("Number of two white in rows:", self.twoWhiteInRow)
        print("Number of three black in rows:", self.threeBlackInRow)
        print("Number of three white in rows:", self.threeWhiteInRow)
        print("Number of four white  in rows:", self.fourWhiteInRow)
        print("Number of four blacks in rows:", self.fourBlackInRow)
        """
        return False

    def checkCols(self):
        colScore = 1
        self.fourInCol = 0
        self.twoWhiteInCol = 0
        self.twoBlackInCol = 0
        self.threeWhiteInCol = 0
        self.threeBlackInCol = 0
        self.fourWhiteInCol = 0
        self.fourBlackInCol = 0
        for j in range(0, Globals.BOARDSIZE):
            colScore = 1
            for i in range(1, Globals.BOARDSIZE):
                if self.board.square[i][j].value == self.board.square[i - 1][j].value != "_":
                    colScore = colScore + 1
                    if colScore == Globals.WIN:
                        return True
                    if colScore == 2 and self.board.square[i + 1][j].value == "_" and self.board.square[i - 2][j].value == "_":
                        if self.board.square[i][j].value == "white":
                            self.twoWhiteInCol += 1
                        else:
                            self.twoBlackInCol += 1
                    if colScore == 3 and self.board.square[i + 1][j].value == "_" and self.board.square[i - 3][j].value == "_":
                        # print("Jestem tu3")
                        if self.board.square[i][j].value == "white":
                            self.threeWhiteInCol += 1
                        else:
                            self.threeBlackInCol += 1
                    if colScore == 4 and (self.board.square[i + 1][j].value == "_" or self.board.square[i - 4][j].value == "_"):
                        #  print("Jestem tu4")
                        if self.board.square[i][j].value == "white":
                            self.fourWhiteInCol += 1
                        else:
                            self.fourBlackInCol += 1
                        self.importantMoves.add((i + 1, j, 690000))
                        self.importantMoves.add((i - 3, j, 690000))
                else:
                    colScore = 1
        """
        print("Number of two white in cols:", self.twoWhiteInCol)
        print("Number of two black in cols:", self.twoBlackInCol)
        print("Number of three white in cols:", self.threeWhiteInCol)
        print("Number of three black in cols:", self.threeBlackInCol)
        print("Number of four white in cols:", self.fourWhiteInCol)
        print("Number of four black in cols:", self.fourBlackInCol)
        """
        return False

    def checkDiagonal(self):
        score = 1
        self.fourWhiteInDiagonal = 0
        self.fourBlackInDiagonal = 0
        self.threeWhiteInDiagonal = 0
        self.threeBlackInDiagonal = 0
        self.twoWhiteInDiagonal = 0
        self.twoBlackInDiagonal = 0
        # 1\
        for i in range(0, Globals.BOARDSIZE):
            score = 1
            for j in range(1, Globals.BOARDSIZE - i):
                if self.board.square[j + i][j].value == self.board.square[j + i - 1][j - 1].value != "_":
                    score = score + 1
                    if score == Globals.WIN:
                        return True
                    if score == 2 and self.board.square[j + i + 1][j + 1].value == "_" and self.board.square[j + i - 2][j - 2].value == "_":
                        if self.board.square[j + i][j].value == "white":
                            self.twoWhiteInDiagonal += 1
                        else:
                            self.twoBlackInDiagonal += 1
                    if score == 3 and self.board.square[j + i + 1][j + 1].value == "_" and self.board.square[j + i - 3][j - 3].value == "_":
                        if self.board.square[j + i][j].value == "white":
                            self.threeWhiteInDiagonal += 1
                        else:
                            self.threeBlackInDiagonal += 1
                    if score == 4 and (self.board.square[j + i + 1][j + 1].value == "_" or self.board.square[j + i - 4][j - 4].value == "_"):
                        if self.board.square[j + i][j].value == "white":
                            self.fourWhiteInDiagonal += 1
                        else:
                            self.fourBlackInDiagonal += 1
                        self.importantMoves.add((j + i + 1, j + 1, 690000))
                        self.importantMoves.add((j + i - 3, j - 3, 690000))
                else:
                    score = 1
        # 2\
        score = 1
        for i in range(0, Globals.BOARDSIZE):
            score = 1
            for j in range(1, Globals.BOARDSIZE - i):
                if self.board.square[j][j + i].value == self.board.square[j - 1][j + i - 1].value != "_":
                    score = score + 1
                    if score == Globals.WIN:
                        return True
                    if score == 2 and self.board.square[j + 1][j + i + 1].value == "_" and self.board.square[j - 2][j + i - 2].value == "_":
                        if self.board.square[j][j + i].value == "white":
                            self.twoWhiteInDiagonal += 1
                        else:
                            self.twoBlackInDiagonal = +1
                    if score == 3 and self.board.square[j + 1][j + i + 1].value == "_" and self.board.square[j - 3][j + i - 3].value == "_":
                        if self.board.square[j][j + i].value == "white":
                            self.threeWhiteInDiagonal += 1
                        else:
                            self.threeBlackInDiagonal = +1
                    if score == 4 and (self.board.square[j + 1][j + i + 1].value == "_" or self.board.square[j - 4][j + i - 4].value == "_"):
                        if self.board.square[j][j + i].value == "white":
                            self.fourWhiteInDiagonal += 1
                        else:
                            self.fourBlackInDiagonal += 1
                        self.importantMoves.add((j + 1, j + i + 1, 690000))
                        self.importantMoves.add((j - 3, j + i - 3, 690000))
                else:
                    score = 1
        # 3/
        score = 1
        for i in range(1, Globals.BOARDSIZE):
            score = 1
            for j in range(0, i):
                if self.board.square[i - j][j].value == self.board.square[i - j - 1][j + 1].value != "_":
                    score = score + 1
                    if score == Globals.WIN:
                        return True
                    if score == 2 and self.board.square[i - j + 1][j - 1].value == "_" and self.board.square[i - j - 2][j + 2].value == "_":
                        if self.board.square[i - j][j].value == "white":
                            self.twoWhiteInDiagonal += 1
                        else:
                            self.twoBlackInDiagonal += 1
                    if score == 3 and self.board.square[i - j + 1][j - 1].value == "_" and self.board.square[i - j - 3][j + 3].value == "_":
                        if self.board.square[i - j][j].value == "white":
                            self.threeWhiteInDiagonal += 1
                        else:
                            self.threeBlackInDiagonal += 1
                    if score == 4 and self.board.square[i - j + 1][j - 1].value == "_" and self.board.square[i - j - 4][j + 4].value == "_":
                        if self.board.square[i - j][j].value == "white":
                            self.fourWhiteInDiagonal += 1
                        else:
                            self.fourBlackInDiagonal += 1
                        self.importantMoves.add((i - j + 1, j - 1, 690000))
                        self.importantMoves.add((i - j - 3, j + 3, 690000))
                else:
                    score = 1

        # 4
        score = 1
        for i in range(0, Globals.BOARDSIZE):
            score = 1
            for j in range(Globals.BOARDSIZE - 1, i, -1):
                if self.board.square[i + (Globals.BOARDSIZE - 1) - j][j].value == \
                        self.board.square[i + (Globals.BOARDSIZE - 1) - j + 1][j - 1].value != "_":
                    score = score + 1
                    if score == Globals.WIN:
                        return True
                    if score == 2 and self.board.square[i + (Globals.BOARDSIZE - 1) - j + 2][j - 2].value != "_" \
                            and self.board.square[i + (Globals.BOARDSIZE - 1) - j - 1][j + 1].value != "_":
                        if self.board.square[i + (Globals.BOARDSIZE - 1) - j][j].value == "white":
                            self.twoWhiteInDiagonal += 1
                        else:
                            self.twoBlackInDiagonal += 1
                    if score == 3 and self.board.square[i + (Globals.BOARDSIZE - 1) - j + 3][j - 3].value != "_" \
                            and self.board.square[i + (Globals.BOARDSIZE - 1) - j - 1][j + 1].value != "_":
                        if self.board.square[i + (Globals.BOARDSIZE - 1) - j][j].value == "white":
                            self.threeWhiteInDiagonal += 1
                        else:
                            self.threeBlackInDiagonal += 1
                    if score == 4 and self.board.square[i + (Globals.BOARDSIZE - 1) - j - 1][j + 1].value != "_" \
                            and self.board.square[i + (Globals.BOARDSIZE - 1) - j + 4][j - 4].value != "_":
                        if self.board.square[i + (Globals.BOARDSIZE - 1) - j][j].value == "white":
                            self.fourWhiteInDiagonal += 1
                        else:
                            self.fourBlackInDiagonal += 1
                        self.importantMoves.add((i + (Globals.BOARDSIZE - 1) - j - 2, j + 2, 690000))
                        self.importantMoves.add((i + (Globals.BOARDSIZE - 1) - j + 2, j - 2, 690000))
                else:
                    score = 1
        """
        print("Number of two white in digonal:", self.twoWhiteInDiagonal)
        print("Number of two black in digonal:", self.twoBlackInDiagonal)
        print("Number of three white in digonal:", self.threeWhiteInDiagonal)
        print("Number of three black in digonal:", self.threeBlackInDiagonal)
        print("Number of four white in digonal:", self.fourWhiteInDiagonal)
        print("Number of four black in digonal:", self.fourBlackInDiagonal)
        """
        return False

    def win(self):
        message("Wygrana", int(Globals.screenWidth / 2), int(Globals.screenHeight / 2 / 5))
        self.run = False
        pygame.display.update()

    def draw(self):
        message("Remis", int(Globals.screenWidth / 2), int(Globals.screenHeight / 2 / 5))
        self.run = False
        pygame.display.update()

    def checkWin(self):
        if self.moveNumber > 1:
            if self.checkRows() or self.checkCols() or self.checkDiagonal():
                return True
        return False

    def checkDraw(self):
        if self.moveNumber == Globals.BOARDSIZE * Globals.BOARDSIZE + 1:
            return True
        else:
            return False

    def addNeighbours(self, i, j):
        if i > 0 and j > 0 and i < Globals.BOARDSIZE - 1 and j < Globals.BOARDSIZE - 1:
            self.board.square[i + 1][j + 1].numberOfNeighboursWhite += 1
            self.board.square[i + 1][j].numberOfNeighboursWhite += 1
            self.board.square[i + 1][j - 1].numberOfNeighboursWhite += 1
            self.board.square[i][j + 1].numberOfNeighboursWhite += 1
            self.board.square[i][j - 1].numberOfNeighboursWhite += 1
            self.board.square[i - 1][j + 1].numberOfNeighboursWhite += 1
            self.board.square[i - 1][j].numberOfNeighboursWhite += 1
            self.board.square[i - 1][j - 1].numberOfNeighboursWhite += 1

    def minusNeighbours(self, i, j):
        if i > 0 and j > 0 and i < Globals.BOARDSIZE - 1 and j < Globals.BOARDSIZE - 1:
            self.board.square[i + 1][j + 1].numberOfNeighboursWhite -= 1
            self.board.square[i + 1][j].numberOfNeighboursWhite -= 1
            self.board.square[i + 1][j - 1].numberOfNeighboursWhite -= 1
            self.board.square[i][j + 1].numberOfNeighboursWhite -= 1
            self.board.square[i][j - 1].numberOfNeighboursWhite -= 1
            self.board.square[i - 1][j + 1].numberOfNeighboursWhite -= 1
            self.board.square[i - 1][j].numberOfNeighboursWhite -= 1
            self.board.square[i - 1][j - 1].numberOfNeighboursWhite -= 1

    def boardSet(self):
        secik = set()
        for i in range(15):
            for j in range(15):
                if self.board.square[i][j].numberOfNeighboursWhite > 0 and self.board.square[i][j].value == "_":
                    secik.add((i, j))
        return secik

    def makeMove(self, i, j):
        if self.onMove == "white":
            self.board.square[i][j].whiteSquare(i, j)
            self.board.square[i][j].value = "white"
            self.onMove = "black"
            pygame.draw.circle(Globals.screen, (0, 0, 0), (700 + 30, 200 + 30), 30)
        else:
            self.board.square[i][j].blackSquare(i, j)
            self.board.square[i][j].value = "black"
            self.onMove = "white"
            pygame.draw.circle(Globals.screen, (255, 255, 255), (700 + 30, 200 + 30), 30)
        self.moveNumber = self.moveNumber + 1
        self.addNeighbours(i, j)

    def minimax(self, board, depth, depthMax, isMaximizing, alpha, beta):
        if self.checkWin():
            if isMaximizing:
                return -10000
            elif isMaximizing is False:
                return 10000
        elif self.checkDraw():
            print("tu ma nie wchodzic")
            return 0
        elif depth == depthMax:
            # print("A teraz jestem w elsie")
            return (
                    (self.fourWhiteInRow + self.fourWhiteInCol + self.fourWhiteInDiagonal) * (-1000)
                    + (self.fourBlackInRow + self.fourBlackInCol + self.fourBlackInDiagonal) * (1000)
                    + (self.threeWhiteInRow + self.threeWhiteInCol + self.threeWhiteInDiagonal) * (-100)
                    + (self.threeBlackInRow + self.threeBlackInCol + self.threeBlackInDiagonal) * (100)
                    + (self.twoWhiteInRow + self.twoWhiteInCol + self.twoWhiteInDiagonal) * (-10)
                    + (self.twoBlackInRow + self.twoBlackInCol + self.twoBlackInDiagonal) * (10)
            )
        minMaxSet = self.boardSet()
        if isMaximizing:
            bestScore = -math.inf
            for i, j in minMaxSet:
                self.board.square[i][j].value = "black"
                self.moveNumber = self.moveNumber + 1
                self.addNeighbours(i, j)
                score = self.minimax(board, depth + 1, Globals.maxDepth, False, alpha, beta)
                self.minusNeighbours(i, j)
                self.board.square[i][j].value = "_"
                self.moveNumber = self.moveNumber - 1
                bestScore = max(score, bestScore)
                alpha = max(alpha, bestScore)
                if beta <= alpha:
                    break
                if bestScore == 10000:
                    break
            return bestScore
        else:
            bestScore = math.inf
            for i, j in minMaxSet:
                self.board.square[i][j].value = "white"
                self.moveNumber = self.moveNumber + 1
                self.addNeighbours(i, j)
                score = self.minimax(board, depth + 1, Globals.maxDepth, True, alpha, beta)
                self.minusNeighbours(i, j)
                self.board.square[i][j].value = "_"
                self.moveNumber = self.moveNumber - 1
                bestScore = min(score, bestScore)
                beta = min(beta, bestScore)
                if beta <= alpha:
                    break
                if bestScore == -10000:
                    break
            return bestScore

    def sort(self, sub_li):
        return (sorted(sub_li, key=lambda x: x[2], reverse=True))

    def forcedMove(self):
        timeStart = time.time()
        forcedSet = self.boardSet()
        # checking winning force move
        print("Checking if there is forced move...")
        for i, j in forcedSet:
            # print("Time spent forced defensive move in depth 0 na board[{}][{}] : {}".format(i, j, time.time() - timeStart))
            self.board.square[i][j].value = "white"
            self.moveNumber = self.moveNumber + 1
            self.addNeighbours(i, j)
            score = self.minimax(self.board, 0, 0, True, -math.inf, math.inf)
            # print("Score dla forced move , Dla board[{}][{}]  score=={}".format(i, j, score))
            self.minusNeighbours(i, j)
            self.board.square[i][j].value = "_"
            self.moveNumber = self.moveNumber - 1
            if score == -10000:
                print("Forced defensive move ! Wykonano ruch na board[{}][{}] Bestscore=={}".format(i, j, score))
                self.makeMove(i, j)
                return True
        print("Not found defensive forced move in depth 0 in time:", time.time() - timeStart)
        if self.moveNumber > 0:
            self.importantMoves.clear()
            for i, j in forcedSet:
                # print("Time spent forced winning move in depth 0 na board[{}][{}] : {}".format(i, j, time.time() - timeStart))
                self.board.square[i][j].value = "black"
                self.moveNumber = self.moveNumber + 1
                self.addNeighbours(i, j)
                score = self.minimax(self.board, 0, 0, False, -math.inf, math.inf)
                self.minusNeighbours(i, j)
                self.board.square[i][j].value = "_"
                self.moveNumber = self.moveNumber - 1
                self.importantMoves.add((i, j, score))
                if score == 10000:
                    print("Forced winning move ! Wykonano ruch na board[{}][{}] Bestscore=={}".format(i, j, score))
                    self.makeMove(i, j)
                    return True
            print("Not found winning forced move in depth 0")
            print("Sorted important moves:", self.sort(self.importantMoves))
        return False

    def playBest(self):
        bestScoreNeighbours = 0
        bestScore = -math.inf
        Imax = 0
        Jmax = 0
        stop = False
        if self.forcedMove():
            pass
        else:
            startTime = time.time()
            # bestSet = self.boardSet()
            # print("caly set:", bestSet)
            secik = self.sort(self.importantMoves)
            print("Important moves", secik)
            for i, j, z in secik:
                if self.board.square[i][j].value == "_" and (time.time() - startTime < Globals.maxMoveTime or bestScore == -10000):
                    self.board.square[i][j].value = "black"
                    self.moveNumber = self.moveNumber + 1
                    self.addNeighbours(i, j)
                    score = self.minimax(self.board, 0, Globals.maxDepth, False, -math.inf, math.inf)
                    self.minusNeighbours(i, j)
                    self.board.square[i][j].value = "_"
                    self.moveNumber = self.moveNumber - 1
                    print("Dla board[{}][{}]  score=={}".format(i, j, score))
                    if score == 10000:
                        Imax = i
                        Jmax = j
                        break
                    if score > bestScore:
                        bestScore = score
                        Imax = i
                        Jmax = j
            print("Wykonano ruch na board[{}][{}] Bestscore=={}".format(Imax, Jmax, bestScore))
            self.makeMove(Imax, Jmax)

    def playgame(self):
        Globals.screen.fill((0, 0, 0))
        self.board.draw()
        pygame.draw.rect(Globals.screen, (102, 51, 0), (700, 200, 60, 60))
        pygame.draw.circle(Globals.screen, (255, 255, 255), (700 + 30, 200 + 30), 30)
        while self.run:
            pygame.display.update()
            pygame.time.delay(100)
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for i in range(0, Globals.BOARDSIZE):
                        for j in range(0, Globals.BOARDSIZE):
                            if self.board.square[i][j].graphic.collidepoint(pos) and self.board.square[i][j].value == '_':
                                if self.onMove == "white":
                                    self.makeMove(i, j)
                                    pygame.display.update()
                                if self.checkWin():
                                    self.win()
                                    break
                                elif self.checkDraw():
                                    self.draw()
                                    break
                                if self.onMove == "black":
                                    starTime = time.time()
                                    self.playBest()
                                    print("Minelo tyle czasu", starTime - time.time())
                                    pygame.display.update()
                                if self.checkWin():
                                    self.win()
                                    break
                                elif self.checkDraw():
                                    self.draw()
                    pygame.display.update()


game = Game()
game.playgame()
time.sleep(5)
sys.exit(0)
