from list_histogram import *
import sys


def sample(histogram):                      # In this example histogram is going to be a list of list
    total_sum = 0                           # Get the total number of frequency in the histogram
    cumulative_probability = 0.0            # cumulative_probability to prevent the function from not picking anything
    for value in histogram:
        total_sum += value[1]

    for value in histogram:
        random_num = random.uniform(0, 1)
        cumulative_probability += value[1]/total_sum  # increment the cumulative_probability by the quotient of the current word to the total word in the histogram
        if cumulative_probability >= random_num:
            return value[0]


def multiple_runs(histogram):
    count_dict = dict()

    for item in histogram:
        count_dict[item[0]] = 0

    for i in range(0, 1000):
        count_dict[sample(histogram)] += 1

    print(count_dict)


if __name__ == "__main__":
    params = sys.argv[1:]   # params is a list of arguments inputted in CL
    sample_histogram = listogram(params)
    multiple_runs(sample_histogram)
