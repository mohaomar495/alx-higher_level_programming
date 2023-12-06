#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        total_score = sum(score * weight for score, weight in my_list)
        total_weight = sum(weight for _, weight in my_list)
        average = total_score / total_weight
        return average
    return 0
