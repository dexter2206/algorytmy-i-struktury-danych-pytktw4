from itertools import islice
import operator

def reduce(collection, func):
    result = collection[0]
    for element in islice(collection, 1, len(collection)):
        result = func(result, element)
    return result


if __name__ == '__main__':
    print(reduce([1, 2, 3, 4], operator.add))
    print(reduce([3, 5, 7, -1], operator.mul))
