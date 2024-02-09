from day_25 import get_entry_value, convert_to_decimal, part1


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
    assert get_entry_value('1121-1110-1=0') == 314159265

def test_convert_to_decimal():
    assert convert_to_decimal(1) == 1

def test_part1():
    assert part1() == 4890
