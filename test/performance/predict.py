import timeit


setup_code = """import src.nn
game = src.nn.GAME_GENERATOR.next()
fen = game.get_random_board_state()
X = game.convert_fen_to_array(fen).reshape(1, -1)
y = [game.int_result]
src.nn.clf.fit(X, y)"""

n = 1000

print(timeit.timeit("src.nn.clf.predict(X)",
                    setup=setup_code, number=n) / n)
