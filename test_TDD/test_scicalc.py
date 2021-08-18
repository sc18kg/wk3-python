from calculator import SciCalc

c = SciCalc()

def test_find_sqrt():
    assert c.find_swrt(100) == 10
    assert c.find_swrt(None) is None
    assert c.find_swrt(25) == 5


def test_find_ceil():
    assert c.find_ceil(12.7) == 13
    assert c.find_ceil(20.2) == 21
    