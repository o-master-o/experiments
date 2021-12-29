import pytest
from old_phone_encoder import send_message

@pytest.mark.parametrize('message, expectations', [
        ('123456789*0#', '1-2-3-4-5-6-7-8-9-*-0-#-'),
        ('1223455677889*0#', '1-2-2-3-4-5-5-6-7-7-8-8-9-*-0-#-'),
        ('1123', '1-1-2-3-'),
        ('111', '1-1-1-'),
        ('1', '1-'),
        ('5', '5-'),
        ('9', '9-'),
        ('*', '*-'),
        ('0', '0-'),
        ('#', '#-'),
        ('##', '#-#-'),
        ('#0', '#-0-'),
    ])
def test_top_row_symbols(message, expectations):
    assert send_message(message) == expectations


@pytest.mark.parametrize('message, expectations', [
        ('', ''),
        (' ', '0'),
        ('a', '2'),
        ('ad', '23'),
        ('adgjmptw\' ', '23456789*0'),
        ('A', '#2'),
        ('A', '#2'),
        ('aD', '2#3'),
        ('aDg', '2#3#4'),
        ('a d', '203'),
    ])
def test_not_repeatable_key_letters_symbols(message, expectations):
    assert send_message(message) == expectations


@pytest.mark.parametrize('message, expectations', [
        ('aa', '2 2'),
        ('aabb', '2 2 22 22'),
        ('aA', '2#2'),
        ('aaBB', '2 2#22 22'),
    ])
def test_repeatable_key_letters_symbols(message, expectations):
    assert send_message(message) == expectations


@pytest.mark.parametrize('message, expectations', [
        ('a7', '27-'),
        ('a7BK', '27-#2255'),
        ('one two three', '666 6633089666084477733 33'),
        ('Def Con 1!', '#3#33 3330#222#666 6601-1111'),
        ('A-z', '#2**#9999'),
        ('QX.JUlwX7bhPZVx3V8l+XOk5lD*pHbOq8!I',
         '#77991588#5559#997-#2244#79999888#993-#888 8-#555***#99666#55 5-555#3*-#7#44#22#666#778-1111#444'),
    ])
def test_random_text(message, expectations):
    assert send_message(message) == expectations
