import pytest

from convert import convert 



def test_convertion():
    assert convert(1) == 149597870700
    assert convert(0) == 0
    assert convert(2.5) == 373994676750.0


def test_error():
    with pytest.raises(TypeError):
        convert("1")

def test_float_convertion():
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-9)
    