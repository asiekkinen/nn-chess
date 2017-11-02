import random
import chess
import numpy as np
import lichess_parser


class Game(object):
    """Full chess game."""

    _piece_to_int = {'p': -1, 'n': -3, 'b': -3, 'r': -5, 'q': -9, 'k': -12,
                     'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 12, '.': 0}
    _result_to_int = {'0-1': -1, '1-0': 1, '1/2-1/2': 0}

    def __init__(self, moves, result):
        """Initialize game.

        Parameters
        ----------
        moves : list of strings
            Each string is a san.
        result : string
            Outcome of the game.
        """
        self._moves = moves
        self._result = result
        self._board = chess.Board()
        self._positions = None

    def play(self):
        """Play the game determined by moves.

        Stores all game positions to self._positions as fens.
        """
        self._positions = []
        for move in self._moves:
            self.board.push_san(move)
            self._positions.append(self.board.fen())

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, fen):
        self._board = chess.Board(fen)

    def convert_fen_to_array(self, fen):
        """Convert board position to an array.

        The array's shape is (65) so that the first 64 values are the board
        squares in the board and each square has a value depending on what pawn
        occupies it.
        """
        board = chess.Board(fen)
        string_representation = board.__str__()
        array = np.empty((65), int)
        for i in range(0, len(string_representation), 2):
            array[i / 2] = self._piece_to_int[string_representation[i]]
        if board.turn:
            array[64] = 1
        else:
            array[64] = -1
        return array

    @property
    def int_result(self):
        return self._result_to_int[self._result]

    def get_random_board_state(self):
        """Get random board state from the played game.

        Requires the play method to be run before."""
        return random.choice(self._positions)

    def convert_array_to_fen(self, array):
        raise NotImplementedError()


def generate_games():
    """Iterator for games.

    Yields
    ------
    Game
    """
    for datafile in lichess_parser.RESOURCE_FILES:
        parser = lichess_parser.LichessParser(datafile)
        for moves, result in parser.games():
            game = Game(moves, result)
            game.play()
            yield game


#def play():
#    parser = LichessParser()
#    for white_moves, black_moves, result in parser.games():
#        game = chess.Board()
#        for white_move, black_move in zip(white_moves, black_moves):
#            game.push_san(white_move)
#            game.push_san(black_move)
#        return game
#
#
#def get_random_board_states():
#    for datafile in files:
#        parser = LichessParser(datafile)
#        for moves, result in parser.games():
#            game = chess.Board()
#            try:
#                end_index = random.randrange(1, len(moves) - 1, 1)
#            except ValueError:
#                continue
#            for move in moves[:end_index]:
#                try:
#                    game.push_san(move)
#                except ValueError:
#                    break
#            else:
#                yield game, result
#
