from collections import namedtuple

import pytest

from chapter_3 import chance_win_single, chance_win_weighted

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
    assert chance_win_single(dp=data["knicks"].win_per, weight=1.0) == 0.5
    assert chance_win_single(dp=data["suns"].win_per, weight=1.0) == 0.7

def test_chance_win_weighted_sum(data):
    assert chance_win_weighted(
        dps=[data["knicks"].win_per, data["knicks"].fans],
        weights=[0.75, 0.05]
    ) == 0.8
    assert chance_win_weighted(
        dps=[data["suns"].win_per, data["suns"].fans],
        weights=[0.75, 0.05]
    ) == 0.6
