from seasons import calculate_minutes, convert_to_words
from datetime import date

def test_calculate_minutes():
    assert calculate_minutes(date(2020, 1, 1)) > 0
    assert calculate_minutes(date.today()) == 0

def test_convert_to_words():
    assert convert_to_words(1000) == "One thousand minutes"
    assert convert_to_words(525600) == "Five hundred twenty-five thousand six hundred minutes"
