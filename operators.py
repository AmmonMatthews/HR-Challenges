#!/bin/python3

import math
import os
import random
import re
import sys
'''
Understand:
    Given three numbers: meal cost, tip percentage of the meal and the tax percentage
    Need to find out the amount of the tip and tax from the meal and then add them together

Plan:
    -create two variables. tax and tip
    -tax = meal * tax_percent/100
    -tip = meal * tip_percednt/100
    -total = meal + tax + tip
    return total

Review: 
    created a total variable
    commetted and spaced code to be cleaner. 
'''
# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tax = meal_cost * (tax_percent/100)
    tip = meal_cost * (tip_percent/100)
    print(round(meal_cost + tax + tip))
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
