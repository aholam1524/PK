from clamp import clamp


def test_value_inside_range():
    assert clamp(5, 0, 10) == 5


def test_value_below_range():
    assert clamp(-5, 0, 10) == 0


def test_value_above_range():
    assert clamp(15, 0, 10) == 10


def test_value_equal_to_low_bound():
    assert clamp(0, 0, 10) == 0


def test_value_equal_to_high_bound():
    assert clamp(10, 0, 10) == 10
