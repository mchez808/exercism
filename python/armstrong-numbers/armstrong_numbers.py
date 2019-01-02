import numpy as np

def is_armstrong(number):
    power = len(str(number))
    return number == sum([int(digit)**power for digit in str(number)])
