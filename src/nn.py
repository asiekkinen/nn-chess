"""Module for training neural network in chess."""
from sklearn.neural_network import MLPRegressor
import numpy as np
import game


GAME_GENERATOR = game.generate_games()


def generate_batch(size):
    """Generate batch of given size.

    Returns the data and the labels

    Parameters
    ----------
    size : int
        Size of the batch.

    Returns
    -------
    tuple
        Array of shape (size, 65) and an array of shape (size)
    """
    X = np.empty((size, 65))
    y = np.empty((size))
    for i in xrange(size):
        game = GAME_GENERATOR.next()
        fen = game.get_random_board_state()
        X[i] = game.convert_fen_to_array(fen)
        y[i] = game.int_result
    return X, y


clf = MLPRegressor(solver='lbfgs', activation='logistic',
                   hidden_layer_sizes=(100, 100, 100))


if __name__ == "__main__":
    X, y = generate_batch(10000)
    clf.fit(X, y)
