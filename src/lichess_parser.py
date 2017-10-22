import os
import re


RESOURCES = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         '../resources/lichess')
files = ['./lichess_db_standard_rated_2014-01.pgn',
         './lichess_db_standard_rated_2013-06.pgn',
         './lichess_db_standard_rated_2013-01.pgn']


class LichessParser(object):
    def __init__(self, filename):
        self.filename = filename

    def games(self):
        with open(self.filename, 'rb') as datafile:
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


def get_datafiles():
    files = os.listdir(RESOURCES)
    return [os.path.join(RESOURCES, filename) for filename in files
            if filename.endswith("pgn")]
