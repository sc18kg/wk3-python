import pytest
from scrabble import Game
from scrabble import ScrabbleHand

s = ScrabbleHand()
g = Game()
@pytest.mark.parametrize("test_word, expected_score",
[
    ("happy", 15),
    ("fog", 7),
    ("frog", 8)
])

def test_calc_score(test_word, expected_score):
    assert g.calc_score(test_word) == expected_score

def test_hand_init_with_7():
    assert len(s.hand) == 7

def test_tile_is_str():
    assert type(s.hand) is str

def test_is_valid_word():
    s = ScrabbleHand()
    g = Game()
    s.tiles = "housety"
    assert s.is_valid_word("house") is True