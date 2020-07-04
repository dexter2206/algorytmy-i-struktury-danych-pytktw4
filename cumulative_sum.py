from typing import List


def cumulative_sum(numbers):
    cum_sums = []
    prev = 0

    for number in numbers:
        cum_sums.append(prev + number)
        prev = cum_sums[-1]

    return cum_sums


def cumulative_sum_copy(numbers: List[int]):
    cum_sums = list(numbers)

    for i in range(1, len(cum_sums)):
        cum_sums[i] += cum_sums[i-1]

    return cum_sums


if __name__ == '__main__':
    print(cumulative_sum_copy([1, 3, 5, 1]))
