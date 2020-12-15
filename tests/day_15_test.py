import pytest
from main.day_15 import solve_1, solve_2


def test_solve_1():
    assert solve_1([1, 3, 2]) == 1
    assert solve_1([2, 1, 3]) == 10
    assert solve_1([1, 2, 3]) == 27
    assert solve_1([2, 3, 1]) == 78
    assert solve_1([3, 2, 1]) == 438
    assert solve_1([3, 1, 2]) == 1836


@pytest.mark.skip(reason="so slow...")
def test_solve_2():
    assert solve_2([0, 3, 6]) == 175594
    assert solve_2([1, 3, 2]) == 2578
    assert (
        solve_2(
            [
                2,
                1,
                3,
            ]
        )
        == 3544142
    )
    assert solve_2([1, 2, 3]) == 261214
    assert solve_2([2, 3, 1]) == 6895259
    assert solve_2([3, 2, 1]) == 18
    assert solve_2([3, 1, 2]) == 362
