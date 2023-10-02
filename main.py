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
    for i in np.arange(MAX_ITERATIONS):
        x_values[i + 1] = logistic(r, x_values[i])
    return x_values


def get_deltas(x_values):
    deltas = np.zeros(MAX_ITERATIONS)
    for i in np.arange(MAX_ITERATIONS - 1):
        deltas[i] = x_values[i + 1] - x_values[i]
    return deltas


def question_a():
    for r in R_VALUES:
        x_values = get_x_values(r)
        iterations_x = np.arange(x_values.size)
        plt.title(f"Value of X against Iterations (r = {r})")
        plt.plot(iterations_x, x_values, color="r")
        plt.xlabel("Iterations")
        plt.ylabel("X")
        plt.show()

        deltas = get_deltas(x_values)
        iterations_delta = np.arange(deltas.size)
        plt.title(f"Value of Deltas against Iterations (r = {r})")
        plt.plot(iterations_delta, deltas, color="g")
        plt.xlabel("Iterations")
        plt.ylabel("Deltas")
        plt.show()

        successors = x_values[1:]
        predecessors = x_values[:-1]
        plt.title(f"Value of Successors against Predecessors (r = {r})")
        plt.xlabel("Predecessors")
        plt.ylabel("Successors")
        plt.plot(predecessors, successors, color="b")
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
