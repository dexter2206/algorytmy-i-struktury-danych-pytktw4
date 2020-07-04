from powers import fast_power_rec
import pytest


@pytest.mark.parametrize("base,exponent,expected_result", [(5, 2, 25), (4, 3, 64), (3, 7, 3 ** 7)])
def test_computes_power_for_base_gt_one(base, exponent, expected_result):
    assert fast_power_rec(base, exponent) == expected_result


def test_powers_of_one_are_equal_one():
    assert fast_power_rec(1, 10) == 1
    assert fast_power_rec(1, 100) == 1


def test_powers_of_zero_are_zero():
    assert fast_power_rec(0, 10) == 0
    assert fast_power_rec(0, 5) == 0


def test_zero_to_zeroth_power_raises_exception():
    with pytest.raises(ValueError):
        fast_power_rec(0, 0)
