from itertools import islice

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    fib = iter(fibonacci())
    for _ in range(10):
        print(next(fib))

    for n in islice(fibonacci(), 10):
        print(n)
