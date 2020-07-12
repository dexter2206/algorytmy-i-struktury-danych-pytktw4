from reduce import reduce
from functools import reduce as reduce2

def gcd(a: int, b: int) -> int:
    if a == 0 and b == 0:
        raise ValueError("GCD is not defined for a = b = 0")
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    numbers = [12, 30, 50, 8]
    print(reduce(numbers, gcd))
    print(reduce2(gcd, numbers))
