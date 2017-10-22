import timeit


setup_code = """import src.game
generator = src.game.generate_games()"""

n = 1000

print(timeit.timeit("generator.next()",
                    setup=setup_code, number=n) / n)
