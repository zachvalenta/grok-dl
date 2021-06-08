###
# 1 input, 1 output [Trask 3.22-27]
###


def chance_win_single(dp, weight):
    return dp * weight


###
# n input, 1 output [Trask 3.28-35]
###


def chance_win_weighted(dps, weights):
    prediction = 0
    for ind, dp in enumerate(dps):
        prediction += dp * weights[ind]
    return round(prediction, 1)


###
# 1 input, n output [Trask 3.36-37]
###


def predict_win_per_fans_from_salary(dp, weights):
    predictions = dict()
    for k, v in weights.items():
        predictions[k] = round(v * dp, 1)
    return predictions
