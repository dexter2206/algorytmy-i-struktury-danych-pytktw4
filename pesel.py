WEIGHTS = 2 * [9, 7, 3, 1] + [9, 7]


def validate(pesel: str) -> bool:
    expected_ctrl = sum(
        weight * int(digit) for digit, weight in zip(pesel, WEIGHTS)
    ) % 10
    return expected_ctrl == int(pesel[-1])


if __name__ == "__main__":
    print(validate("88062213538"))
