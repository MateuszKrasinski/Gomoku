import math
import time
import copy
from Globals import BOARDSIZE, maxDepth, maxMoveTime, numberOfCheckedSquares, numberOfChosenToMinimax
from CheckBoardState import CheckBoardState

IMPORTANT = math.inf
WHITE_WIN = -100000
BLACK_WIN = 100000


class AI():
    def __init__(self, board, moveNumber):
        self.b = board
        self.moveNumber = moveNumber
        self.arbiter = CheckBoardState(self.b)
        self.optionalMoves = [set() for i in range(maxDepth + 1)]
        self.importantMoves = [set() for i in range(maxDepth + 1)]
        self.PlayedMoves = set()
        self.PredictedMoves = set()

    def miniMax(self, b, depth, depthMax, isMaximizing, alpha, beta):
        if self.arbiter.checkWin(depth):
            if isMaximizing:
                return WHITE_WIN
            elif isMaximizing is False:
                return BLACK_WIN
        elif self.arbiter.checkDraw(self.moveNumber):
            return 0
        elif depth == depthMax:
            return self.arbiter.evaluate(depth)
        minMaxSet = self.optionalMoves[depth]
        secik = []
        if isMaximizing:
            bestScore = -math.inf
            for i, j in minMaxSet:
                score = self.miniMax(b, depth, depth, False, alpha, beta)
                secik.append((i, j, score))
                secik = self.sortMovesByEvaluation(secik)
            for i, j, z in secik[:(numberOfCheckedSquares - depth)]:
                self.b.square[i][j].value = "black"
                self.moveNumber = self.moveNumber + 1
                self.addNeighboursSquares(i, j, depth + 1)
                score = self.miniMax(b, depth + 1, maxDepth, False, alpha, beta)
                self.removeNeighboursSquares(i, j, depth + 1)
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
                score = self.miniMax(b, depth, depth, True, alpha, beta)
                secik.append((i, j, score))
            secik = self.sortMovesByEvaluation(secik)
            for i, j, z in secik[:numberOfCheckedSquares - depth]:
                self.b.square[i][j].value = "white"
                self.moveNumber += 1
                self.addNeighboursSquares(i, j, depth + 1)
                score = self.miniMax(b, depth + 1, maxDepth, True, alpha, beta)
                self.removeNeighboursSquares(i, j, depth + 1)
                self.b.square[i][j].value = "_"
                self.moveNumber -= 1
                bestScore = min(score, bestScore)
                beta = min(beta, bestScore)
                if beta <= alpha:
                    break
                if bestScore == WHITE_WIN:
                    break
            return bestScore
    """sorting optional moves by evaluation of position after first predicted move"""
    def sortMovesByEvaluation(self, sub_li):
        return (sorted(sub_li, key=lambda x: x[2], reverse=True))
    """ if there is win in one move just play it else if opponent can win just move to block this move"""
    def forcedMove(self):
        self.importantMoves[0].clear()
        print("Checking if there is forced move...")
        for i, j in self.optionalMoves[0]:
            if self.b.square[i][j].value == "_":
                self.b.square[i][j].value = "black"
                score = self.miniMax(self.b, 1, 1, False, -math.inf, math.inf)
                self.b.square[i][j].value = "_"
                self.importantMoves[0].add((i, j, score))
            if score == BLACK_WIN:
                print("Forced winning move ! Wykonano ruch na b[{}][{}] Bestscore=={}".format(i, j, score))
                return i, j
        print("Not found winning forced move in depth 0")
        for i, j in self.optionalMoves[0]:
            if self.b.square[i][j].value == "_":
                self.b.square[i][j].value = "white"
                score = self.miniMax(self.b, 0, 0, True, -math.inf, math.inf)
                self.b.square[i][j].value = "_"
                if score == WHITE_WIN:
                    print("Forced defensive move ! Wykonano ruch na b[{}][{}] Bestscore=={}".format(i, j, score))
                    return i, j
        print("Not found defensive forced move in depth 0 in time:")
        return False

    """Checking if there is force move else searching best move using minimax on selected initially sorted moves """
    def playBest(self):
        bestScore = -math.inf
        iMax = 0
        jMax = 0
        if self.forcedMove() is not False:
            i, j = self.forcedMove()
            self.PlayedMoves.add((i, j))
            self.importantMoves[0].clear()
            return i, j
        else:
            startTime = time.time()
            secik = self.sortMovesByEvaluation(self.importantMoves[0])
            print("{}Important moves1{}".format(len(secik), secik))
            print("{}Optional moves{}".format(len(self.optionalMoves[0]), self.optionalMoves[0]))
            for i, j, score in secik[:numberOfChosenToMinimax]:
                if self.b.square[i][j].value == "_" and (time.time() - startTime < maxMoveTime or bestScore == WHITE_WIN):
                    self.b.square[i][j].value = "black"
                    self.moveNumber = self.moveNumber + 1
                    self.addNeighboursSquares(i, j, 1)
                    score = self.miniMax(self.b, 1, maxDepth, False, -math.inf, math.inf)
                    self.removeNeighboursSquares(i, j, 1)
                    self.b.square[i][j].value = "_"
                    self.moveNumber -= 1
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
            self.importantMoves[0].clear()
            self.PlayedMoves.add((iMax, jMax))
            self.optionalMoves[1] = copy.deepcopy(self.optionalMoves[2])
            self.optionalMoves[2] = copy.deepcopy(self.optionalMoves[3])
            self.optionalMoves[3] = copy.deepcopy(self.optionalMoves[4])
            self.optionalMoves[4] = copy.deepcopy(self.optionalMoves[5])
            self.optionalMoves[5] = copy.deepcopy(self.optionalMoves[6])
            return iMax, jMax
    """Adding new squares to Optional Moves after move or in minimax predictions"""
    def addNeighboursSquares(self, i, j, depth):
        if i > 0 and j > 0 and j < BOARDSIZE - 1 and i < BOARDSIZE - 1:
            self.Neihbours = {(i + 1, j + 1), (i + 1, j - 1), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j + 1), (i - 1, j - 1), (i - 1, j)}
        self.optionalMoves[depth] = self.optionalMoves[depth - 1].union(self.Neihbours.difference(self.optionalMoves[depth - 1]))
        self.optionalMoves[depth].difference_update(self.PlayedMoves)
        self.PredictedMoves.add((i, j))
        self.optionalMoves[depth].difference_update((self.PredictedMoves))
    """recall changes after addNeighboursSquares in Minimax"""
    def removeNeighboursSquares(self, i, j, depth):
        self.optionalMoves[depth] = copy.deepcopy(self.optionalMoves[depth - 1])
        self.PredictedMoves.remove((i, j))
