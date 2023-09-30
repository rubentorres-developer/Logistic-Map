import numpy as np
import matplotlib.pyplot as plt

MAX_ITERATIONS = 100
R_VALUES = np.array([0.9, 1.8, 2.6, 3.2, 3.9, 3.99])
STARTING_X = 0.5


def logistic(r, x):
    return r * x * (1 - x)


def get_x_values(r):
    x_values = np.zeros(MAX_ITERATIONS + 1)
    x_values[0] = STARTING_X
    for i in range(MAX_ITERATIONS):
        x_values[i + 1] = logistic(r, x_values[i])
    return x_values


def get_deltas(res):
    deltas = []
    for i in range(len(res) - 1):
        d = res[i + 1] - res[i]
        deltas.append(d)
    return deltas


def question_a():
    for r in R_VALUES:
        x_values = get_x_values(r)
        it = [y for y in range(len(x_values))]
        plt.title(f"Value of X against Iterations (r = {r})")
        plt.plot(it, x_values)
        plt.show()

        deltas = get_deltas(x_values)
        it2 = [y for y in range(len(deltas))]
        plt.title(f"Value of Deltas against Iterations (r = {r})")
        plt.plot(it2, deltas)
        plt.show()

        plt.title(f"Value of Successors against Predecessors (r = {r})")
        plt.plot(x_values[1:], x_values[:-1])
        plt.show()

        plt.close()
    return True


def question_b():
    return True


def main():
    question_a()
    return True


if __name__ == "__main__":
    main()
