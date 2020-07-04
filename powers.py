def power(base, exponent):
    if base == 0 and exponent == 0:
        raise ValueError("Cannot compute 0 ** 0")
    result = 1
    for _ in range(exponent):
        result *= base

    return result


def power_rec(base, exponent):
    if base == 0 and exponent != 0:
        return 0
    elif base == 0 and exponent == 0:
        raise ValueError()
    elif exponent == 0:
        return 1
    return base * power_rec(base, exponent-1)

def fast_power_rec(base, exponent):
    if base == 0 and exponent != 0:
        return 0
    elif base == 0 and exponent == 0:
        raise ValueError()
    elif exponent == 0:
        return 1
    tmp = fast_power_rec(base, exponent // 2)
    tmp *= tmp
    if exponent % 2 == 1:
        tmp *= base
    return tmp
