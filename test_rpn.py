import operator
from rpn import evaluate_rpn, OPERATORS
from unittest.mock import Mock


def test_calls_operators_with_correct_arguments():
    operators = {
        "+": Mock(wraps=operator.add),
        "*": Mock(wraps=operator.mul),
        "-": Mock(wraps=operator.sub)
    }

    evaluate_rpn([5, 4, 1, "-", "*", 2, "+"], operators)

    operators["-"].assert_called_once_with(4, 1)
    operators["*"].assert_called_once_with(5, 3)
    operators["+"].assert_called_once_with(15, 2)


def test_computes_correct_value():
    assert evaluate_rpn([5, 4, 1, "-", "*", 2, "+"], OPERATORS) == 17

