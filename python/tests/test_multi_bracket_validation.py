import pytest
from challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_1 ():
    actual = multi_bracket_validation('()[[Extra Characters]]')
    expected = True
    assert actual == expected

def test_2 ():
    actual = multi_bracket_validation('{}{Code}[Fellows](())')
    expected = True
    assert actual == expected

def test_3 ():
    actual = multi_bracket_validation('[({}]')
    expected = False
    assert actual == expected

def test_4 ():
    actual = multi_bracket_validation('(](')
    expected = False
    assert actual == expected

def test_5 ():
    actual = multi_bracket_validation('{(})')
    expected = False
    assert actual == expected



