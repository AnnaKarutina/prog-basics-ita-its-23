import pytest
from function import *


@pytest.mark.timeout(1.0)
def test_func(capsys):
    func()
    captured = capsys.readouterr()
    assert captured.out == "I´m inside the function\n"

@pytest.mark.timeout(1.0)
def test_my_name_is(capsys):
    assert my_name_is("Mari") is None, "Function should return None (you can omit return statement)"
    assert capsys.readouterr().out == "My name is Mari\n", "Check the spelling of the print out string"
    assert my_name_is("Tiit") is None
    assert capsys.readouterr().out == "My name is Tiit\n"
    assert my_name_is("ab58z0Olw") is None
    assert capsys.readouterr().out == "My name is ab58z0Olw\n"

@pytest.mark.timeout(1.0)
def test_sum_six():
    assert sum_six(0) == 6
    assert sum_six(6) == 12
    assert sum_six(10) == 16

@pytest.mark.timeout(1.0)
def test_sum_numbers():
    assert sum_numbers(5, 5) == 10
    assert sum_numbers(0, 50) == 50
    assert sum_numbers(17, 28) == 45

@pytest.mark.timeout(1.0)
def test_usd_to_eur():
    assert usd_to_eur(1.25) == 1.0
    assert usd_to_eur(100) == 80.0
    assert usd_to_eur(69) == 55.2
    assert usd_to_eur(12450) == 9960.0
    assert usd_to_eur(0) == 0.0
