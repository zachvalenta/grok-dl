from collections import namedtuple

import pytest

from chapter_3 import chance_win_single, chance_win_weighted, use_salary_to_predict_win_per_and_fans


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
    """
    chance of winning current game based on winning percentage
    """
    win_per_weight = 1.0
    assert chance_win_single(dp=data["knicks"].win_per, weight=win_per_weight) == 0.5
    assert chance_win_single(dp=data["suns"].win_per, weight=win_per_weight) == 0.7


###
# n input, 1 output
###

def test_chance_win_weighted_sum(data):
    """
    chance of winning current game based on weighted sum of winning percentage + number of fans
    """
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
    """
    * use salary to predict winning percentage and number of fans
    * Suns: winning percentage what you'd expect but far fewer fans than expected
    * Knicks: winning percentage what you'd expect but somewhat more fans than expected
    """
    assert use_salary_to_predict_win_per_and_fans(dp=data["suns"].salary, weights={"win_per": 0.01, "fans": 0.1}) == {'win_per': 0.7, 'fans': 7.0}
    assert use_salary_to_predict_win_per_and_fans(dp=data["knicks"].salary, weights={"win_per": 0.01, "fans": 0.1}) == {'win_per': 0.5, 'fans': 5.0}
