import os
import re


RESOURCES = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         '../resources/lichess')
RESOURCE_FILES = [filename for filename in os.listdir(RESOURCES)
                  if filename.endswith('.pgn')]


class LichessParser(object):
    def __init__(self, filepath):
        """Initialize parser.

        Parameters
        ----------
        filepath : string
            Filepath to a .pgn file.
        """
        self.filepath = filepath

    def games(self):
        """Iterator for moves and results of games.

        Yields
        ------
        tuple
            List of moves (strings) and result (string)
        """
        with open(self.filepath, 'rb') as datafile:
            for line in datafile:
                line = line.strip()
                if not line.startswith("1. ") or "{" in line:
                    continue
                moves = line.split(" ")
                result = moves[-1]
                parsed_moves = []
                for move in moves[:-1]:
                    if re.search(r'[0-9]+\.', move):
                        continue
                    else:
                        parsed_moves.append(move)
                yield parsed_moves, result
