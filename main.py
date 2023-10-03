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


def plot_graphs(x_axis_label, x_axis_values, y_axis_label, y_axis_values, r, c, p):
    plt.subplot(3, 1, p)
    plt.title(f"Value of {y_axis_label} against {x_axis_label} (r = {r})")
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.plot(x_axis_values, y_axis_values, color=c, marker=".")


def question_a():
    for r in R_VALUES:
        plt.figure()

        x_values = get_x_values(r)
        iterations_x = np.arange(x_values.size)
        plot_graphs("Iterations", iterations_x, "X", x_values, r, "r", 1)

        deltas = get_deltas(x_values)
        iterations_delta = np.arange(1, deltas.size + 1)
        plot_graphs(
            "Iterations",
            iterations_delta,
            r"$\Delta X = X_{n + 1} - X_n$",
            deltas,
            r,
            "g",
            2,
        )

        successors = x_values[1:]
        predecessors = x_values[:-1]
        plot_graphs(r"$X_n$", predecessors, r"$X_{n + 1}$", successors, r, "b", 3)

        plt.tight_layout()
        plt.savefig(f"./images/plot_r_{r}.png")
        plt.show()
        plt.close()


def question_b():
    plt.figure()

    epsilon = 0.001
    delta = -0.1
    threshold_diff = 0.5
    chaos_regime_start = 3.6

    iteration_list = []
    r_list = []

    r = 4
    while r >= chaos_regime_start:
        x_a = STARTING_X
        x_b = x_a - epsilon

        iterations = 0
        while abs(x_a - x_b) < threshold_diff:
            x_a = logistic(r, x_a)
            x_b = logistic(r, x_b)
            iterations += 1

        iteration_list.append(iterations)
        r_list.append(r)
        r += delta

    plt.title("Value of R against Iterations")
    plt.xlabel("Iterations")
    plt.ylabel("R")
    plt.plot(iteration_list, r_list, color="r", marker=".")
    plt.savefig(f"./images/chaotic_behavior_analysis.png")
    plt.show()
    plt.close()


def main():
    question_a()
    question_b()


if __name__ == "__main__":
    main()
