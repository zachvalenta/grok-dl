import pytest

from chapter_3 import chance_win_single

def test_chance_win_single():
    assert chance_win_single(datapoint=0.5) == 0.5
    assert chance_win_single(datapoint=0.7) == 0.7
