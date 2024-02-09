from day_25 import get_digit_value, get_entry_value, part1


def test_get_digit_value():
    assert get_digit_value('1', 0) == 1
    assert get_digit_value('1', 1) == 5
    assert get_digit_value('2', 1) == 10
    assert get_digit_value('1', 2) == 25
    assert get_digit_value('2', 2) == 50
    assert get_digit_value('1', 3) == 125


def test_get_entry_value():
    assert get_entry_value('1') == 1
    assert get_entry_value('10') == 5
    assert get_entry_value('20') == 10
    assert get_entry_value('100') == 25
    assert get_entry_value('-') == -1
    assert get_entry_value('=') == -2
    assert get_entry_value('10-') == 24
    assert get_entry_value('10=') == 23
    assert get_entry_value('1-0') == 20
    assert get_entry_value('2=-01') == 1250-250-25+0+1 # 976


def test_part1():
    assert part1()
