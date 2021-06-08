from collections import namedtuple

import pytest

from chapter_3 import chance_win_single, chance_win_weighted, predict_win_per_fans_from_salary


@pytest.fixture(scope="module")
def data():
    Team = namedtuple("team", "win_per fans salary")
    bulls = Team(win_per=0.45, fans=4.5, salary=45)
    knicks = Team(win_per=0.5, fans=8.5, salary=50)
    suns = Team(win_per=0.7, fans=0.75, salary=70)
    return {
        "bulls": bulls,
        "knicks": knicks,
        "suns": suns,
    }


###
# 1 input, 1 output
###

def test_chance_win_single(data):
    win_per_weight = 1.0
    assert chance_win_single(dp=data["knicks"].win_per, weight=win_per_weight) == 0.5
    assert chance_win_single(dp=data["suns"].win_per, weight=win_per_weight) == 0.7


###
# n input, 1 output
###

def test_chance_win_weighted_sum(data):
    win_per_weight = 0.75
    fan_weight = 0.05
    assert (
        chance_win_weighted(
            dps=[data["knicks"].win_per, data["knicks"].fans], weights=[win_per_weight, fan_weight]
        )
        == 0.8
    )
    assert (
        chance_win_weighted(
            dps=[data["suns"].win_per, data["suns"].fans], weights=[win_per_weight, fan_weight]
        )
        == 0.6
    )

###
# 1 input, n output
###

def test_predict_salary(data):
    # meaning, Suns have fewer fans and Knicks more than you'd expected based on salary
    assert predict_win_per_fans_from_salary(dp=data["suns"].salary, weights={"win_per": 0.01, "fans": 0.1}) == {'win_per': 0.7, 'fans': 7.0}
    assert predict_win_per_fans_from_salary(dp=data["knicks"].salary, weights={"win_per": 0.01, "fans": 0.1}) == {'win_per': 0.5, 'fans': 5.0}
