from collections import namedtuple

import pytest

from chapter_3 import chance_win_single, chance_win_weighted, use_salary_to_predict_win_per_and_fans, use_salary_fans_wp_to_predict_gate_ratings


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
    assert chance_win_single(wp=data["knicks"].win_per, weight=win_per_weight) == 0.5
    assert chance_win_single(wp=data["suns"].win_per, weight=win_per_weight) == 0.7


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
            factors=[data["knicks"].win_per, data["knicks"].fans], weights=[win_per_weight, fan_weight]
        )
        == 0.8
    )
    assert (
        chance_win_weighted(
            factors=[data["suns"].win_per, data["suns"].fans], weights=[win_per_weight, fan_weight]
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
    assert use_salary_to_predict_win_per_and_fans(salary=data["suns"].salary, weights={"win_per": 0.01, "fans": 0.1}) == {'win_per': 0.7, 'fans': 7.0}
    assert use_salary_to_predict_win_per_and_fans(salary=data["knicks"].salary, weights={"win_per": 0.01, "fans": 0.1}) == {'win_per': 0.5, 'fans': 5.0}

###
# n input, n output [Trask 3.38-43]
###
def test_use_salary_fans_wp_to_predict_gate_ratings(data):
    use_salary_fans_wp_to_predict_gate_ratings(factors={"salary": data["suns"].salary, "fans": data["suns"].fans }, weights={"gate": [0.10, 1], "ratings": [0.01, 1]}) == {'gate': 7.8, 'ratings': 1.5}
