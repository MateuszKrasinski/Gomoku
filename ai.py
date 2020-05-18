import math
import time
import check_board_state
WHITE_WIN = -1000000
BLACK_WIN = 1000000
MAX_MOVE_TIME = 6
MAX_DEPTH = 5
NUMBER_OF_CHECKED_SQUARES = 10
NUMBER_OF_CHECKED_SQUARES_IN_MINI_MAX = 11
BOARDSIZE = 15  # stala rozmiar planszy
WHITE="white"
BLACK="black"


class AI():
    def __init__(self, board, move_number):
        self.board = board
        self.move_number = move_number
        self.arbiter = check_board_state.CheckBoardState(self.board)
        self.optional_moves = [set() for i in range(MAX_DEPTH + 1)]
        self.important_moves = [set() for i in range(MAX_DEPTH + 1)]
        self.predicted_moves = set()
        self.played_moves = set()
        self.good_moves = []

    def mini_max(self, b, depth, max_depth, is_maximizing, alpha, beta):
        if self.arbiter.check_win():
            if is_maximizing:
                return WHITE_WIN
            return BLACK_WIN
        if self.arbiter.check_draw(self.move_number):
            return 0
        if depth == max_depth:
            return self.arbiter.evaluate()
        min_max_set = self.optional_moves[depth]
        secik = []
        if is_maximizing:
            best_score = -math.inf
            for i, j in min_max_set:
                self.board[i][j] = BLACK
                score = self.mini_max(self.board, depth, depth, False, alpha, beta)
                self.board[i][j] = "_"
                secik.append((i, j, score))
            secik = self.sort_moves_by_evaluation(secik, True)
            for i, j, evaluation in secik[:(NUMBER_OF_CHECKED_SQUARES_IN_MINI_MAX - depth)]:
                self.board[i][j] = BLACK
                self.move_number = self.move_number + 1
                self.add_neighbours_squares(i, j, depth + 1, self.played_moves)
                score = self.mini_max(self.board, depth + 1, MAX_DEPTH, False, alpha,
                                      beta)
                self.remove_neigbours_squares(i, j, depth + 1)
                self.board[i][j] = "_"
                self.move_number = self.move_number - 1
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
                if best_score == BLACK_WIN:
                    break
            return best_score

        best_score = math.inf
        for i, j in min_max_set:
            self.board[i][j] = WHITE
            score = self.mini_max(self.board, depth, depth, True, alpha, beta)
            self.board[i][j] = "_"
            secik.append((i, j, score))
        secik = self.sort_moves_by_evaluation(secik, False)
        for i, j, evaluation in secik[:(NUMBER_OF_CHECKED_SQUARES_IN_MINI_MAX - depth)]:
            self.board[i][j] = WHITE
            self.move_number += 1
            self.add_neighbours_squares(i, j, depth + 1, self.played_moves)
            score = self.mini_max(self.board, depth + 1, MAX_DEPTH, True, alpha, beta)
            self.remove_neigbours_squares(i, j, depth + 1)
            self.board[i][j] = "_"
            self.move_number -= 1
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
            if best_score == WHITE_WIN:
                break
        return best_score

    def sort_moves_by_evaluation(self, sub_li, is_maximazing):
        return sorted(sub_li, key=lambda x: x[2], reverse=is_maximazing)

    def forced_move(self):
        self.important_moves[0].clear()
        print("Checking if there is forced move...")
        if self.move_number == 0 and len(self.optional_moves[0]) == 0:
            self.optional_moves[0].add((7, 7))
        for i, j in self.optional_moves[0]:
            if self.board[i][j] == "_":
                self.board[i][j] = BLACK
                score = self.mini_max(self.board, 0, 0, False, -math.inf,
                                      math.inf)
                self.board[i][j] = "_"
                self.important_moves[0].add((i, j, score))
            if score == BLACK_WIN:
                print(
                    "Forced winning move ! Wykonano ruch na b[{}][{}] best_score=={}".format(i, j, score))
                return i, j
        print("Not found winning forced move in depth 0")
        for i, j in self.optional_moves[0]:
            if self.board[i][j] == "_":
                self.board[i][j] = WHITE
                score = self.mini_max(self.board, 1, 1, True, -math.inf,
                                      math.inf)
                self.board[i][j] = "_"
                if score == WHITE_WIN:
                    print(
                        "Forced defensive move ! Wykonano ruch na b[{}][{}] best_score=={}".format(
                            i, j, score))
                    return i, j
        print("Not found defensive forced move in depth 0 in time:")
        return False

    def play_best(self, played_moves):
        self.played_moves = played_moves
        print("played_moves moves:", len(self.played_moves))
        best_score = -math.inf
        if self.forced_move() is not False:
            i, j = self.forced_move()
            self.important_moves[0].clear()
            return i, j
        self.mini_max(self.board, 0, 0, True, -math.inf, math.inf)
        start_time = time.time()
        self.good_moves = self.arbiter.good_moves
        secik = self.sort_moves_by_evaluation(self.important_moves[0], True)
        print("{}Important moves{}".format(len(secik), secik))
        print("         Good moves:", self.good_moves)
        print("Suma: ", self.good_moves + secik)
        secik = self.good_moves + secik
        for i, j, score in secik:
            if self.board[i][j] == "_" and ( time.time() - start_time < MAX_MOVE_TIME):
                self.board[i][j] = BLACK
                self.move_number = self.move_number + 1
                self.add_neighbours_squares(i, j, 1, self.played_moves)
                score = self.mini_max(self.board, 1, MAX_DEPTH, False,
                                      -math.inf,
                                      math.inf)
                self.remove_neigbours_squares(i, j, 1)
                self.board[i][j] = "_"
                self.move_number -= 1
                print("Dla b[{}][{}]  score=={}".format(i, j, score))
                if score == BLACK_WIN:
                    best_move = i, j
                    break
                if score > best_score:
                    best_score = score
                    best_move = i, j
        print("Wykonano ruch na b[{}][{}] best_score=={}".format(best_move[0],best_move[1],
                         best_score))
        self.important_moves[0].clear()
        print("Predicted:", len(self.predicted_moves))
        return best_move

    """Adding new squares to Optional Moves after move or in mini_max predictions"""

    def add_neighbours_squares(self, i, j, depth, played_moves):
        if i > 0 and j > 0 and j < BOARDSIZE - 1 and i < BOARDSIZE - 1:
            self.neihbours = {(i + 1, j + 1), (i + 1, j - 1), (i + 1, j),
                              (i, j - 1), (i, j + 1), (i - 1, j + 1),
                              (i - 1, j - 1), (i - 1, j)}
        self.played_moves = played_moves
        if depth == 0:
            self.optional_moves[0] = self.optional_moves[depth].union(
                self.neihbours)
            self.optional_moves[depth].difference_update(self.played_moves)
        elif depth != 0:
            self.predicted_moves.add((i, j))
            self.optional_moves[depth] = self.optional_moves[depth - 1].union(
                self.neihbours)
            self.optional_moves[depth].difference_update(self.played_moves)
            self.optional_moves[depth].difference_update((self.predicted_moves))

        if depth == 0:
            print("{}Optional moves{}".format(len(self.optional_moves[0]),
                                              self.optional_moves[0]))


    def remove_neigbours_squares(self, i, j, depth):
        self.optional_moves[depth] = (self.optional_moves[depth - 1])
        self.predicted_moves.remove((i, j))
