import operator

OPERATORS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


def evaluate_rpn(expression, operators):
    operands = []

    for symbol in expression:
        if symbol in operators:
            second, first = operands.pop(), operands.pop()
            operands.append(operators[symbol](first, second))
        else:
            operands.append(symbol)

    return operands.pop()


if __name__ == "__main__":
    print(evaluate_rpn([5, 2, 1, "-", "*", 4, "+"], OPERATORS))
