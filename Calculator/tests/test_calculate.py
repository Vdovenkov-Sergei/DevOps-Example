import pytest
from src.calculate import calculate


@pytest.mark.parametrize(
    "x, y, operator, result",
    [
        (0, 10, "-", -10),
        (5, 5, "*", 25),
        (-115, -5, "/", 23),
        (10, 60, "+", 70),
        (50, 2, "^", 2500),
    ],
)
def test_calculate_success(x, y, operator, result):
    assert calculate(x, y, operator) == result


@pytest.mark.parametrize(
    "x, y, operator, result",
    [
        (5, 8, "-", -6),
        (5, 5, "*", 21),
        (-37, 15, "/", 4),
        (10, 67, "+", 70),
        (5, 5, "^", 500),
    ],
)
def test_calculate_fail(x, y, operator, result):
    assert calculate(x, y, operator) != result


def test_calculate_exception(capsys):
    with pytest.raises(ZeroDivisionError):
        calculate(5, 0, "/")
    with pytest.raises(KeyError):
        calculate(16, 5, "%")
