import pygame, sys, time, Globals, math
import board
from Globals import BOARDSIZE, WIN, screenWidth, screenHeight, screen, maxDepth, maxMoveTime
from pygame import mixer
import random

IMPORTANT = math.inf
WHITE_WIN = -10000
BLACK_WIN = 10000
pygame.init()
pygame.display.set_caption('Gomoku')


def message(what, x, y):
    font = pygame.font.Font("freesansbold.ttf", 72)
    text = font.render(what, True, (0, 128, 0))
    screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))


class Game:
    def __init__(self):
        self.run = True
        self.moveNumber = 1
        self.b = board.Board()
        self.onMove = "white"
        self.importantMoves = set()
        self.optionalMoves=[set() for i in range(maxDepth+1)]

    def checkRows(self):
        self.fourBlackInRow = 0
        self.fourWhiteInRow = 0
        self.threeWhiteInRow = 0
        self.threeBlackInRow = 0
        self.twoWhiteInRow = 0
        self.twoBlackInRow = 0
        for i in range(0, BOARDSIZE):
            rowScore = 1
            for j in range(1, BOARDSIZE):
                if self.b.square[i][j].value == self.b.square[i][j - 1].value != "_":
                    rowScore += 1
                else:
                    if rowScore == WIN:
                        return True
                    elif rowScore == 4:
                        if self.b.square[i][j].value == "white":
                            self.fourWhiteInRow += 1
                        else:
                            self.fourBlackInRow += 1
                    elif rowScore == 3:
                        if self.b.square[i][j].value == "white":
                            self.threeWhiteInRow += 1
                        else:
                            self.threeBlackInRow += 1
                    elif rowScore == 2:
                        if self.b.square[i][j].value == "white":
                            self.twoWhiteInRow += 1
                        else:
                            self.twoBlackInRow += 1
                    rowScore = 1
        return False

    def checkCols(self):
        self.twoWhiteInCol = 0
        self.twoBlackInCol = 0
        self.threeWhiteInCol = 0
        self.threeBlackInCol = 0
        self.fourWhiteInCol = 0
        self.fourBlackInCol = 0
        for j in range(0, BOARDSIZE):
            colScore = 1
            for i in range(1, BOARDSIZE):
                if self.b.square[i][j].value == self.b.square[i - 1][j].value != "_":
                    colScore += 1
                else:
                    if colScore == WIN:
                        return True
                    elif colScore == 2:
                        if self.b.square[i][j].value == "white":
                            self.twoWhiteInCol += 1
                        else:
                            self.twoBlackInCol += 1
                    elif colScore == 3:
                        if self.b.square[i][j].value == "white":
                            self.threeWhiteInCol += 1
                        else:
                            self.threeBlackInCol += 1
                    elif colScore == 4:
                        if self.b.square[i][j].value == "white":
                            self.fourWhiteInCol += 1
                        else:
                            self.fourBlackInCol += 1
                    colScore = 1
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
        for i in range(0, BOARDSIZE):
            diagonalScore = 1
            for j in range(1, BOARDSIZE - i):
                if self.b.square[j + i][j].value == self.b.square[j + i - 1][j - 1].value != "_":
                    diagonalScore += 1
                else:
                    if diagonalScore == WIN:
                        return True
                    elif diagonalScore == 2:
                        if self.b.square[j + i][j].value == "white":
                            self.twoWhiteInDiagonal += 1
                        else:
                            self.twoBlackInDiagonal += 1
                    elif diagonalScore == 3:
                        if self.b.square[j + i][j].value == "white":
                            self.threeWhiteInDiagonal += 1
                        else:
                            self.threeBlackInDiagonal += 1
                    elif diagonalScore == 4:
                        if self.b.square[j + i][j].value == "white":
                            self.fourWhiteInDiagonal += 1
                        else:
                            self.fourBlackInDiagonal += 1
                    diagonalScore = 1
        # 2\
        diagonalScore = 1
        for i in range(0, BOARDSIZE):
            diagonalScore = 1
            for j in range(1, BOARDSIZE - i):
                if self.b.square[j][j + i].value == self.b.square[j - 1][j + i - 1].value != "_":
                    diagonalScore = diagonalScore + 1
                else:
                    if diagonalScore == WIN:
                        return True
                    elif diagonalScore == 2:
                        if self.b.square[j][j + i].value == "white":
                            self.twoWhiteInDiagonal += 1
                        else:
                            self.twoBlackInDiagonal = +1
                    elif diagonalScore == 3:
                        if self.b.square[j][j + i].value == "white":
                            self.threeWhiteInDiagonal += 1
                        else:
                            self.threeBlackInDiagonal = +1
                    elif diagonalScore == 4:
                        if self.b.square[j][j + i].value == "white":
                            self.fourWhiteInDiagonal += 1
                        else:
                            self.fourBlackInDiagonal += 1
                    diagonalScore = 1
        # 3/
        for i in range(1, BOARDSIZE):
            diagonalScore = 1
            for j in range(0, i):
                if self.b.square[i - j][j].value == self.b.square[i - j - 1][j + 1].value != "_":
                    diagonalScore += 1
                else:
                    if diagonalScore == WIN:
                        return True
                    elif diagonalScore == 2:
                        if self.b.square[i - j][j].value == "white":
                            self.twoWhiteInDiagonal += 1
                        else:
                            self.twoBlackInDiagonal += 1
                    elif diagonalScore == 3:
                        if self.b.square[i - j][j].value == "white":
                            self.threeWhiteInDiagonal += 1
                        else:
                            self.threeBlackInDiagonal += 1
                    elif diagonalScore == 4:
                        if self.b.square[i - j][j].value == "white":
                            self.fourWhiteInDiagonal += 1
                        else:
                            self.fourBlackInDiagonal += 1
                    diagonalScore = 1

        # 4
        for i in range(0, BOARDSIZE):
            diagonalScore = 1
            for j in range(BOARDSIZE - 1, i, -1):
                if self.b.square[i + (BOARDSIZE - 1) - j][j].value == \
                        self.b.square[i + (BOARDSIZE - 1) - j + 1][j - 1].value != "_":
                    diagonalScore += 1
                else:
                    if diagonalScore == WIN:
                        return True
                    elif diagonalScore == 2:
                        if self.b.square[i + (BOARDSIZE - 1) - j][j].value == "white":
                            self.twoWhiteInDiagonal += 1
                        else:
                            self.twoBlackInDiagonal += 1
                    elif diagonalScore == 3:
                        if self.b.square[i + (BOARDSIZE - 1) - j][j].value == "white":
                            self.threeWhiteInDiagonal += 1
                        else:
                            self.threeBlackInDiagonal += 1
                    elif diagonalScore == 4:
                        if self.b.square[i + (BOARDSIZE - 1) - j][j].value == "white":
                            self.fourWhiteInDiagonal += 1
                        else:
                            self.fourBlackInDiagonal += 1
                    diagonalScore = 1
        return False

    def messageWin(self):
        message("Wygrana", int(screenWidth / 2), int(screenHeight / 2 / 5))
        self.run = False
        pygame.display.update()

    def messageDraw(self):
        message("Remis", int(screenWidth / 2), int(screenHeight / 2 / 5))
        self.run = False
        pygame.display.update()

    def checkWin(self):
        if self.moveNumber > 1:
            if self.checkRows() or self.checkCols() or self.checkDiagonal():
                return True
        return False

    def checkDraw(self):
        if self.moveNumber == BOARDSIZE * BOARDSIZE + 1:
            return True
        else:
            return False

    def addNeighbours(self, i, j,depth):
        if i > 0 and j > 0 and i < BOARDSIZE - 1 and j < BOARDSIZE - 1:
            self.b.square[i + 1][j + 1].numberOfNeighboursWhite += 1
            self.b.square[i + 1][j].numberOfNeighboursWhite += 1
            self.b.square[i + 1][j - 1].numberOfNeighboursWhite += 1
            self.b.square[i][j + 1].numberOfNeighboursWhite += 1
            self.b.square[i][j - 1].numberOfNeighboursWhite += 1
            self.b.square[i - 1][j + 1].numberOfNeighboursWhite += 1
            self.b.square[i - 1][j].numberOfNeighboursWhite += 1
            self.b.square[i - 1][j - 1].numberOfNeighboursWhite += 1
            self.optionalMoves[depth].add((i + 1,j + 1))
            self.optionalMoves[depth].add((i + 1,j))
            self.optionalMoves[depth].add((i + 1,j-1))
            self.optionalMoves[depth].add((i ,j -1))
            self.optionalMoves[depth].add((i ,j + 1))
            self.optionalMoves[depth].add((i - 1,j + 1))
            self.optionalMoves[depth].add((i - 1,j ))
            self.optionalMoves[depth].add((i - 1,j - 1))

    def minusNeighbours(self, i, j):
        if i > 0 and j > 0 and i < BOARDSIZE - 1 and j < BOARDSIZE - 1:
            self.b.square[i + 1][j + 1].numberOfNeighboursWhite -= 1
            self.b.square[i + 1][j].numberOfNeighboursWhite -= 1
            self.b.square[i + 1][j - 1].numberOfNeighboursWhite -= 1
            self.b.square[i][j + 1].numberOfNeighboursWhite -= 1
            self.b.square[i][j - 1].numberOfNeighboursWhite -= 1
            self.b.square[i - 1][j + 1].numberOfNeighboursWhite -= 1
            self.b.square[i - 1][j].numberOfNeighboursWhite -= 1
            self.b.square[i - 1][j - 1].numberOfNeighboursWhite -= 1

    def bSet(self):
        secik = set()
        for i in range(15):
            for j in range(15):
                if self.b.square[i][j].numberOfNeighboursWhite > 0 and self.b.square[i][j].value == "_":
                    secik.add((i, j))
        return secik

    def makeMove(self, i, j):
        if self.onMove == "white":
            self.b.square[i][j].whiteSquare(i, j)
            self.b.square[i][j].value = "white"
            self.onMove = "black"
            pygame.draw.circle(screen, (0, 0, 0), (700 + 30, 200 + 30), 30)
        else:
            self.b.square[i][j].blackSquare(i, j)
            self.b.square[i][j].value = "black"
            self.onMove = "white"
            pygame.draw.circle(screen, (255, 255, 255), (700 + 30, 200 + 30), 30)
        self.moveNumber = self.moveNumber + 1
        self.addNeighbours(i, j,0)

    def miniMax(self, b, depth, depthMax, isMaximizing, alpha, beta):
        if self.checkWin():
            if isMaximizing:
                return WHITE_WIN
            elif isMaximizing is False:
                return BLACK_WIN
        elif self.checkDraw():
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
        minMaxSet = self.bSet()
        if isMaximizing:
            bestScore = -math.inf
            for i, j in minMaxSet:
                self.b.square[i][j].value = "black"
                self.moveNumber = self.moveNumber + 1
                self.addNeighbours(i, j,depth+1)
                score = self.miniMax(b, depth + 1, maxDepth, False, alpha, beta)
                self.minusNeighbours(i, j)
                self.b.square[i][j].value = "_"
                self.moveNumber = self.moveNumber - 1
                bestScore = max(score, bestScore)
                alpha = max(alpha, bestScore)
                if beta <= alpha:
                    break
                if bestScore == BLACK_WIN:
                    break
            return bestScore
        else:
            bestScore = math.inf
            for i, j in minMaxSet:
                self.b.square[i][j].value = "white"
                self.moveNumber = self.moveNumber + 1
                self.addNeighbours(i, j,depth+1)
                score = self.miniMax(b, depth + 1, maxDepth, True, alpha, beta)
                self.minusNeighbours(i, j)
                self.b.square[i][j].value = "_"
                self.moveNumber = self.moveNumber - 1
                bestScore = min(score, bestScore)
                beta = min(beta, bestScore)
                if beta <= alpha:
                    break
                if bestScore == WHITE_WIN:
                    break
            return bestScore

    def sort(self, sub_li):
        return (sorted(sub_li, key=lambda x: x[2], reverse=True))

    def forcedMove(self):
        forcedSet = self.bSet()
        # checking winning force move
        print("Checking if there is forced move...")
        for i, j in forcedSet:
            self.b.square[i][j].value = "white"
            self.moveNumber = self.moveNumber + 1
            self.addNeighbours(i, j,1)
            score = self.miniMax(self.b, 0, 0, True, -math.inf, math.inf)
            self.minusNeighbours(i, j)
            self.b.square[i][j].value = "_"
            self.moveNumber = self.moveNumber - 1
            if score == WHITE_WIN:
                print("Forced defensive move ! Wykonano ruch na b[{}][{}] Bestscore=={}".format(i, j, score))
                self.makeMove(i, j)
                return True
        print("Not found defensive forced move in depth 0 in time:")
        self.importantMoves.clear()
        for i, j in forcedSet:
            # print("Time spent forced winning move in depth 0 na b[{}][{}] : {}".format(i, j, time.time() - timeStart))
            self.b.square[i][j].value = "black"
            self.moveNumber = self.moveNumber + 1
            self.addNeighbours(i, j,1)
            score = self.miniMax(self.b, 0, 0, False, -math.inf, math.inf)
            self.minusNeighbours(i, j)
            self.b.square[i][j].value = "_"
            self.moveNumber = self.moveNumber - 1
            self.importantMoves.add((i, j, score))
            if score == BLACK_WIN:
                print("Forced winning move ! Wykonano ruch na b[{}][{}] Bestscore=={}".format(i, j, score))
                self.makeMove(i, j)
                return True
        print("Not found winning forced move in depth 0")
        return False

    def playBest(self):
        bestScore = -math.inf
        iMax = 0
        jMax = 0
        if self.forcedMove():
            pass
        else:
            startTime = time.time()
            secik = self.sort(self.importantMoves)
            print("{}Important moves{}".format( len(secik),secik))
            print("{}Optional moves{}".format( len(self.optionalMoves[0]),self.optionalMoves[0]))
            print()
            for i, j, z in secik:
                if self.b.square[i][j].value == "_" and (time.time() - startTime < maxMoveTime or bestScore == WHITE_WIN):
                    self.b.square[i][j].value = "black"
                    self.moveNumber = self.moveNumber + 1
                    self.addNeighbours(i, j, 1)
                    score = self.miniMax(self.b, 0, maxDepth, False, -math.inf, math.inf)
                    self.minusNeighbours(i, j)
                    self.b.square[i][j].value = "_"
                    self.moveNumber = self.moveNumber - 1
                    print("Dla b[{}][{}]  score=={}".format(i, j, score))
                    if score == BLACK_WIN:
                        iMax = i
                        jMax = j
                        break
                    if score > bestScore:
                        bestScore = score
                        iMax = i
                        jMax = j
            print("Wykonano ruch na b[{}][{}] Bestscore=={}".format(iMax, jMax, bestScore))
            self.makeMove(iMax, jMax)

    def playgame(self):
        screen.fill((0, 0, 0))
        self.b.draw()
        pygame.draw.rect(screen, (102, 51, 0), (700, 200, 60, 60))
        pygame.draw.circle(screen, (255, 255, 255), (700 + 30, 200 + 30), 30)
        while self.run:
            pygame.display.update()
            pygame.time.delay(100)
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for i in range(0, BOARDSIZE):
                        for j in range(0, BOARDSIZE):
                            if self.b.square[i][j].graphic.collidepoint(pos) and self.b.square[i][j].value == '_':
                                if self.onMove == "white":
                                    self.makeMove(i, j)
                                    pygame.display.update()
                                if self.checkWin():
                                    self.messageWin()
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
                                    self.messageWin()
                                    break
                                elif self.checkDraw():
                                    self.draw()
                    pygame.display.update()


game = Game()
game.playgame()
time.sleep(5)
sys.exit(0)