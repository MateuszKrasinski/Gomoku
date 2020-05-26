"""Module contains AI class which ensure artificial intelligence working correctly"""
import math
import time
import operator
import collections

import constants
import check_board_state

WHITE_WIN = -1000000
BLACK_WIN = 1000000
MAX_MOVE_TIME_SECONDS = 6
MAX_DEPTH = 5
NUMBER_OF_CHECKED_SQUARES = 10
NUMBER_OF_CHECKED_SQUARES_IN_MINI_MAX = 11
PlayedMovesInGame = collections.namedtuple("PlayedMovesInGame", "i j ")


class BasePlayer:
    """Base class"""

    def __init__(self, name, stone_color):
        self.name = name
        self.stone_color = stone_color

    def make_move(self):
        """Virtual function"""


class HumanPlayer(BasePlayer):
    """Class creates human player with name and stone_color and method to make move."""

    def make_move(self, pos, gui_board, game_board):
        """Method returns clicked move by the user (i,j)."""
        for i in range(0, constants.BOARD_SIZE):
            for j in range(0, constants.BOARD_SIZE):
                if gui_board[i][j].graphic.collidepoint(
                        pos) and game_board[i][j] == constants.EMPTY:
                    return i, j
        return None


class AiPlayer(BasePlayer):
    """Class contains all needed attributes and methods to create artificial intelligence player."""

    def __init__(self, screen, board, stone_color, name="AI"):
        """Init with board from game module and all needed attributes to make ai optimal.
        Attributes:
        arbiter:   Class which allows to check if game is finished
        squares_with_neighbours: Set contains all squares with neighbours , list index is
        depth during mini_max algorithm we also checked squares with neighbours
        squares_with_neighbours_sorted:Above set sorted by mini_max evaluation after one move
        self.played_moves_in_game: all moves played in game during adding new squares to
        squares_with_neighbours need to remove played moves from this set
        threatening_squares: from CheckBoardState moves to deal with open three stones situation.
        """
        super().__init__(name, stone_color)
        self.screen = screen
        self.game_board = board
        self.arbiter = check_board_state.CheckBoardState(self.screen, self.game_board)
        self.squares_with_neighbours = [set() for i in range(MAX_DEPTH + 1)]
        self.squares_with_neighbours_sorted = [set() for i in range(MAX_DEPTH + 1)]
        self.predicted_moves_in_mini_max = set()
        self.played_moves_in_game = PlayedMovesInGame
        self.threatening_squares = []

    def mini_max(self, board, depth, max_depth, is_maximizing, alpha=-math.inf, beta=math.inf):
        """Methods return tuple (i,j) with best evaluation of position based on given arguments.

        NUMBER_OF_CHECKED_SQUARES_IN_MINI_MAX and NUMBER_OF_CHECKED_SQUARES allows as to
        minimize branching factor which on such a big board is really fast growing up.
        """
        if self.arbiter.check_win():
            if is_maximizing:
                return WHITE_WIN
            return BLACK_WIN
        if self.arbiter.check_draw():
            return 0
        if depth == max_depth:
            return self.arbiter.evaluate()
        min_max_set = self.squares_with_neighbours[depth]
        evaluated_min_max_set = []
        if is_maximizing:
            best_score = -math.inf
            for i, j in min_max_set:
                board[i][j] = constants.BLACK
                score = self.mini_max(board, depth, depth, False, alpha, beta)
                board[i][j] = constants.EMPTY
                evaluated_min_max_set.append((i, j, score))
            evaluated_min_max_set = sort_moves_by_evaluation(evaluated_min_max_set, True)
            for i, j, evaluation in evaluated_min_max_set[:(NUMBER_OF_CHECKED_SQUARES_IN_MINI_MAX -
                                                            depth)]:
                board[i][j] = constants.BLACK
                self.add_neighbours_squares(i, j, depth + 1, self.played_moves_in_game)
                score = self.mini_max(board, depth + 1, MAX_DEPTH, False, alpha,
                                      beta)
                self.remove_neighbours_squares(i, j, depth + 1)
                board[i][j] = constants.EMPTY
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
                if best_score == BLACK_WIN:
                    break
            return best_score

        best_score = math.inf
        for i, j in min_max_set:
            board[i][j] = constants.WHITE
            score = self.mini_max(board, depth, depth, True, alpha, beta)
            board[i][j] = constants.EMPTY
            evaluated_min_max_set.append((i, j, score))
        evaluated_min_max_set = sort_moves_by_evaluation(evaluated_min_max_set, False)
        for i, j, evaluation in evaluated_min_max_set[:(NUMBER_OF_CHECKED_SQUARES_IN_MINI_MAX -
                                                        depth)]:
            board[i][j] = constants.WHITE
            self.add_neighbours_squares(i, j, depth + 1, self.played_moves_in_game)
            score = self.mini_max(board, depth + 1, MAX_DEPTH, True, alpha, beta)
            self.remove_neighbours_squares(i, j, depth + 1)
            board[i][j] = constants.EMPTY
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
            if best_score == WHITE_WIN:
                break
        return best_score

    def forced_move(self):
        """Method checks winning or losing forced move and if there is return move as tuple(i,j)

        Firstly plays one move with stone color on move on all squares_with_neighbours if found
        win just return this move if else plays one move with opponent stone color if found opponent
        win just return this move to defend it.
        """
        self.squares_with_neighbours_sorted[0].clear()
        if len(self.squares_with_neighbours[0]) == 0:
            self.squares_with_neighbours[0].add((7, 7))
        for i, j in self.squares_with_neighbours[0]:
            if self.game_board[i][j] == constants.EMPTY:
                self.game_board[i][j] = constants.BLACK
                score = self.mini_max(self.game_board, 0, 0, False, -math.inf,
                                      math.inf)
                self.game_board[i][j] = constants.EMPTY
                self.squares_with_neighbours_sorted[0].add((i, j, score))
            if score == BLACK_WIN:
                return i, j
        for i, j in self.squares_with_neighbours[0]:
            if self.game_board[i][j] == constants.EMPTY:
                self.game_board[i][j] = constants.WHITE
                score = self.mini_max(self.game_board, 1, 1, True, -math.inf,
                                      math.inf)
                self.game_board[i][j] = constants.EMPTY
                if score == WHITE_WIN:
                    return i, j
        return False

    def make_move(self, game_board, played_moves, black_color=True):
        """Method returns best move as tuple (i,j), first using forced_move() else mini_max()."""
        self.game_board = game_board
        self.played_moves_in_game = played_moves
        self.arbiter = check_board_state.CheckBoardState(self.screen, self.game_board)
        self.squares_with_neighbours[0].clear()
        for i, j in self.played_moves_in_game:
            self.add_neighbours_squares(i, j, 0, self.played_moves_in_game)
        best_score = -math.inf
        if self.forced_move() is not False:
            i, j = self.forced_move()
            self.squares_with_neighbours_sorted[0].clear()
            return i, j
        self.mini_max(self.game_board, 0, 0, True, -math.inf, math.inf)
        start_time = time.time()
        self.threatening_squares = self.arbiter.good_moves
        evaluated_min_max_set = sort_moves_by_evaluation(self.squares_with_neighbours_sorted[0],
                                                         black_color)
        for i, j, score in self.threatening_squares:
            for item in evaluated_min_max_set:
                if i == item[0] and j == item[1]:
                    evaluated_min_max_set.remove(item)
        print("All considered moves: ", self.threatening_squares + evaluated_min_max_set)
        evaluated_min_max_set = self.threatening_squares + evaluated_min_max_set
        for i, j, score in evaluated_min_max_set:
            if self.game_board[i][j] == constants.EMPTY and (
                    time.time() - start_time < MAX_MOVE_TIME_SECONDS):
                self.game_board[i][j] = constants.BLACK
                self.add_neighbours_squares(i, j, 1, self.played_moves_in_game)
                score = self.mini_max(self.game_board, 1, MAX_DEPTH, False)
                self.remove_neighbours_squares(i, j, 1)
                self.game_board[i][j] = constants.EMPTY
                print("At board[{}][{}]  evaluation={}".format(i, j, score))
                if score == BLACK_WIN:
                    best_move = i, j
                    break
                if score > best_score:
                    best_score = score
                    best_move = i, j
        print("Played move on  board[{}][{}] evaluation={}".format(best_move[0], best_move[1],
                                                                   best_score))
        self.squares_with_neighbours_sorted[0].clear()
        return best_move

    def add_neighbours_squares(self, i, j, depth, played_moves):
        """Adding to set self.squares_with_neighbours new squares

        Firstly union neighbours set and squares_with_neighbours after it checking if in this set
        squares was played or predicted in mini_max algorithm and removing this moves.
        """
        down, top, left, right = 1, 1, 1, 1
        if i <= 0:
            top = 0
        if j <= 0:
            left = 0
        if j >= constants.BOARD_SIZE - 1:
            right = 0
        if i >= constants.BOARD_SIZE - 1:
            down = 0
        neighbours = {(i - top, j + right), (i - top, j - left), (i - top, j),
                      (i, j - left), (i, j + right), (i + down, j + right),
                      (i + down, j - left), (i + down, j)}
        self.played_moves_in_game = played_moves
        if depth == 0:
            self.squares_with_neighbours[0] = self.squares_with_neighbours[depth].union(neighbours)
            self.squares_with_neighbours[depth].difference_update(self.played_moves_in_game)
        elif depth != 0:
            self.predicted_moves_in_mini_max.add((i, j))
            self.squares_with_neighbours[depth] = self.squares_with_neighbours[depth - 1].union(
                neighbours)
            self.squares_with_neighbours[depth].difference_update(self.played_moves_in_game)
            self.squares_with_neighbours[depth].difference_update(
                self.predicted_moves_in_mini_max)

    def remove_neighbours_squares(self, i, j, depth):
        """Removing from set self.squares_with_neighbours squares added in mini_max."""
        self.squares_with_neighbours[depth] = self.squares_with_neighbours[depth - 1]
        self.predicted_moves_in_mini_max.remove((i, j))


def sort_moves_by_evaluation(sub_li, is_maximazing):
    """Sort moves by evaluation from mini_max algorithm."""
    return sorted(sub_li, key=operator.itemgetter(2), reverse=is_maximazing)
