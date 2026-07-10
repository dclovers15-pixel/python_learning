from calculater2 import squared


def test_squared():
    assert squared(2) == 4
    assert squared(-3) == 9
    assert squared(0) == 0
    assert squared(1.5) == 0