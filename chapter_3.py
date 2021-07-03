###
# 1 input, 1 output [Trask 3.22-27]
###

def chance_win_single(dp, weight):
    """
    chance of winning current game based on winning percentage
    >>> chance_win_single(dp=0.5, weight=1.0)
    0.5
    """
    return dp * weight

###
# n input, 1 output [Trask 3.28-35]
###

def chance_win_weighted(dps, weights):
    """
    chance of winning current game based on weighted sum of winning percentage + number of fans 
    >>> chance_win_weighted(dps=[0.5, 8.5], weights=[0.75, 0.05])
    0.8
    """
    prediction = 0
    for ind, dp in enumerate(dps):
        prediction += dp * weights[ind]
    return round(prediction, 1)

###
# 1 input, n output [Trask 3.36-37]
###

def use_salary_to_predict_win_per_and_fans(dp, weights):
    """
    use salary to predict winning percentage and number of fans
    >>> use_salary_to_predict_win_per_and_fans(dp=70, weights={"win_per": 0.01, "fans": 0.1})
    {'win_per': 0.7, 'fans': 7.0}
    """
    predictions = dict()
    for k, v in weights.items():
        predictions[k] = round(v * dp, 1)
    return predictions
