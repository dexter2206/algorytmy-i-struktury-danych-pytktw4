def factorial(n):
    if n < 0:
        raise ValueError("Factorial is defined for nonnegative integers.")
    if n <= 1:
        return 1
    return n * factorial(n-1)


if __name__ == '__main__':
    print(factorial(6))
