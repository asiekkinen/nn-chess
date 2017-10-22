import timeit
import matplotlib.pyplot as plt


setup_code = """import src.nn"""

n = 1
x = range(10, 500, 10)
y = []

for i in x:
    print(i)
    y.append(timeit.timeit("src.nn.generate_batch({})".format(i),
                           setup=setup_code, number=n) / n)
plt.plot(x, y)
plt.show()
