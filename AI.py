import math
import time
from CheckBoardState import CheckBoardState

WHITE_WIN = -math.inf
BLACK_WIN = math.inf
maxMoveTime = 6
maxDepth = 5
numberOfCheckedSquares = 10
numberOfCheckedSquaresInMiniMax = 11
BOARDSIZE = 15  # stala rozmiar planszy


class AI():
    def __init__(self, board, moveNumber):
        self.board = board
        self.moveNumber = moveNumber
        self.arbiter = CheckBoardState(self.board)
        self.optionalMoves = [set() for i in range(maxDepth + 1)]
        self.importantMoves = [set() for i in range(maxDepth + 1)]
        self.PredictedMoves = set()
        self.PlayedMoves = set()
        self.goodMoves = []

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
                self.board[i][j] = "black"
                score = self.miniMax(b, depth, depth, False, alpha, beta)
                self.board[i][j] = "_"
                secik.append((i, j, score))
            secik = self.sortMovesByEvaluation(secik, True)
            for i, j, z in secik[:(numberOfCheckedSquaresInMiniMax - depth)]:
                self.board[i][j] = "black"
                self.moveNumber = self.moveNumber + 1
                self.addNeighboursSquares(i, j, depth + 1, self.PlayedMoves)
                score = self.miniMax(b, depth + 1, maxDepth, False, alpha, beta)
                self.removeNeighboursSquares(i, j, depth + 1)
                self.board[i][j] = "_"
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
                self.board[i][j] = "white"
                score = self.miniMax(b, depth, depth, True, alpha, beta)
                self.board[i][j] = "_"
                secik.append((i, j, score))
            secik = self.sortMovesByEvaluation(secik, False)
            for i, j, z in secik[:(numberOfCheckedSquaresInMiniMax - depth)]:
                self.board[i][j] = "white"
                self.moveNumber += 1
                self.addNeighboursSquares(i, j, depth + 1, self.PlayedMoves)
                score = self.miniMax(b, depth + 1, maxDepth, True, alpha, beta)
                self.removeNeighboursSquares(i, j, depth + 1)
                self.board[i][j] = "_"
                self.moveNumber -= 1
                bestScore = min(score, bestScore)
                beta = min(beta, bestScore)
                if beta <= alpha:
                    break
                if bestScore == WHITE_WIN:
                    break
            return bestScore

    def sortMovesByEvaluation(self, sub_li, isMaximazing):
        return (sorted(sub_li, key=lambda x: x[2], reverse=isMaximazing))

    def forcedMove(self):
        self.importantMoves[0].clear()
        print("Checking if there is forced move...")
        if self.moveNumber == 0 and len(self.optionalMoves[0]) == 0:
            self.optionalMoves[0].add((7, 7))
        for i, j in self.optionalMoves[0]:
            if self.board[i][j] == "_":
                self.board[i][j] = "black"
                score = self.miniMax(self.board, 0, 0, False, -math.inf, math.inf)
                self.board[i][j] = "_"
                self.importantMoves[0].add((i, j, score))
            if score == BLACK_WIN:
                print(
                    "Forced winning move ! Wykonano ruch na b[{}][{}] Bestscore=={}".format(
                        i, j, score))
                return i, j
        print("Not found winning forced move in depth 0")
        for i, j in self.optionalMoves[0]:
            if self.board[i][j] == "_":
                self.board[i][j] = "white"
                score = self.miniMax(self.board, 1, 1, True, -math.inf, math.inf)
                self.board[i][j] = "_"
                if score == WHITE_WIN:
                    print(
                        "Forced defensive move ! Wykonano ruch na b[{}][{}] Bestscore=={}".format(
                            i, j, score))
                    return i, j
        print("Not found defensive forced move in depth 0 in time:")
        return False

    def playBest(self, playedMoves):
        self.PlayedMoves = playedMoves
        bestMove = tuple()
        print("Played moves:", len(self.PlayedMoves))
        bestScore = -math.inf
        if self.forcedMove() is not False:
            i, j = self.forcedMove()
            self.importantMoves[0].clear()
            return i, j
        else:
            self.miniMax(self.board, 0, 0, True, -math.inf, math.inf)
            startTime = time.time()
            self.goodMoves = self.arbiter.goodMoves
            secik = self.sortMovesByEvaluation(self.importantMoves[0], True)
            print("{}Important moves{}".format(len(secik), secik))
            print("         Good moves:", self.goodMoves)
            print("Suma: ", self.goodMoves + secik)
            secik = self.goodMoves + secik
            # print("{}Optional moves{}".format(len(self.optionalMoves[0]), self.optionalMoves[0]))
            for i, j, score in secik[:numberOfCheckedSquares]:
                if self.board[i][j] == "_" and (
                        time.time() - startTime < maxMoveTime or bestScore == WHITE_WIN):
                    self.board[i][j] = "black"
                    self.moveNumber = self.moveNumber + 1
                    self.addNeighboursSquares(i, j, 1, self.PlayedMoves)
                    score = self.miniMax(self.board, 1, maxDepth, False, -math.inf,
                                         math.inf)
                    self.removeNeighboursSquares(i, j, 1)
                    self.board[i][j] = "_"
                    self.moveNumber -= 1
                    print("Dla b[{}][{}]  score=={}".format(i, j, score))
                    if score == BLACK_WIN:
                        bestMove = (i, j)
                        break
                    if score > bestScore:
                        bestScore = score
                        bestMove = i, j
            print("Wykonano ruch na b[{}][{}] Bestscore=={}".format(bestMove[0],
                                                                    bestMove[1],
                                                                    bestScore))
            self.importantMoves[0].clear()
            print("Predicted:", len(self.PredictedMoves))
            return bestMove

    """Adding new squares to Optional Moves after move or in minimax predictions"""

    def addNeighboursSquares(self, i, j, depth, playedMoves):
        if i > 0 and j > 0 and j < BOARDSIZE - 1 and i < BOARDSIZE - 1:
            self.Neihbours = {(i + 1, j + 1), (i + 1, j - 1), (i + 1, j),
                              (i, j - 1), (i, j + 1), (i - 1, j + 1),
                              (i - 1, j - 1), (i - 1, j)}
        self.PlayedMoves = playedMoves
        if depth == 0:
            self.optionalMoves[0] = self.optionalMoves[depth].union(
                self.Neihbours)
            self.optionalMoves[depth].difference_update(self.PlayedMoves)
        elif depth != 0:
            self.PredictedMoves.add((i, j))
            self.optionalMoves[depth] = self.optionalMoves[depth - 1].union(
                self.Neihbours)
            self.optionalMoves[depth].difference_update(self.PlayedMoves)
            self.optionalMoves[depth].difference_update((self.PredictedMoves))

        if depth == 0:
            print("{}Optional moves{}".format(len(self.optionalMoves[0]),
                                              self.optionalMoves[0]))

    """recall changes after addNeighboursSquares in Minimax"""

    def removeNeighboursSquares(self, i, j, depth):
        self.optionalMoves[depth] = (self.optionalMoves[depth - 1])
        self.PredictedMoves.remove((i, j))
