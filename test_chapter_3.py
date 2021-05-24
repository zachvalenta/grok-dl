from collections import namedtuple

import pytest

from chapter_3 import chance_win_single

@pytest.fixture(scope="module")
def data():
    Team = namedtuple('team', 'win_per fans')
    bulls = Team(win_per=0.45, fans=2.5)
    knicks = Team(win_per=0.5, fans=8.5)
    suns = Team(win_per=0.7, fans=0.75)
    return {
        "bulls": bulls,
        "knicks": knicks,
        "suns": suns,
    }

def test_chance_win_single(data):
    assert chance_win_single(wp=data["knicks"].win_per) == 0.5
    assert chance_win_single(wp=data["suns"].win_per) == 0.7
