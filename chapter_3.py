###
# 1 input, 1 output [Trask 3.22-27]
###

def chance_win_single(wp, weight):
    """
    chance of winning current game based on winning percentage
    >>> chance_win_single(wp=0.5, weight=1.0)
    0.5
    """
    return wp * weight

###
# n input, 1 output [Trask 3.28-35]
###

def chance_win_weighted(factors, weights):
    """
    chance of winning current game based on weighted sum of winning percentage + number of fans 
    >>> chance_win_weighted(factors=[0.5, 8.5], weights=[0.75, 0.05])
    0.8
    """
    prediction = 0
    for ind, factor in enumerate(factors):
        prediction += factor * weights[ind]
    return round(prediction, 1)

###
# 1 input, n output [Trask 3.36-37]
###

def use_salary_to_predict_win_per_and_fans(salary, weights):
    """
    use salary to predict winning percentage and number of fans
    >>> use_salary_to_predict_win_per_and_fans(salary=70, weights={"win_per": 0.01, "fans": 0.1})
    {'win_per': 0.7, 'fans': 7.0}
    """
    predictions = dict()
    for k, v in weights.items():
        predictions[k] = round(v * salary, 1)
    return predictions

###
# n input, n output [Trask 3.38-43]
###

def use_salary_fans_wp_to_predict_gate_ratings(factors, weights):
    """
    use salary and fans to predict gate and ratings
    >>> use_salary_fans_wp_to_predict_gate_ratings(factors={"salary": 70, "fans": 0.75}, weights={"gate": [0.10, 1], "ratings": [0.01, 1]})
    {'gate': 7.8, 'ratings': 1.5}
    """
    predictions = dict()
    for k, val in weights.items():
        predictions[k] = round((val[0] * factors["salary"]) + (val[1] * factors["fans"]), 1)
    return predictions
