import concurrent.futures
import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def choose_rand_num():
    """
    :return: random int between 1 and 10
    """
    return random.randint(1, 10)


def calculate_histogram(draws_num=100):
    """
    Choose a random number draw_num times
    :param draws_num: how many times draw takes place
    :return: x_axis and y_axis to be plotted
    """

    draws = np.zeros(draws_num, dtype=int)
    for i in range(draws_num):
        draws[i] = choose_rand_num()

    counter = Counter()
    for result in draws:
        counter[result] = counter[result] + 1

    sorted_counter = {k: v for k, v in sorted(list(counter.items()))}

    x_axis = list(sorted_counter.keys())
    y_axis = list(sorted_counter.values())

    return x_axis, y_axis


def run_calc():
    """
    Running threads and showing results
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as thread:
        new_thread = thread.submit(calculate_histogram, 100)

    x_axis, y_axis = new_thread.result()

    # hist, bin_edges = np.histogram(y_axis, bins=50, density=False)
    # bin_width = bin_edges[2] - bin_edges[1]
    # print("Bin width = ", bin_width)

    # plt.figure()
    # plt.plot(bin_edges[:-1], hist, color="green", label="histogrammer")
    # plt.show()

    fig, ax = plt.subplots()
    ax.stem(x_axis, y_axis, use_line_collection=True)
    ax.set_title("Number of times the value was drawed in function of drawed value")
    plt.show()

if __name__ == '__main__':
    run_calc()
    #calculate_histogram(draws_num=100)