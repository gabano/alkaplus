# simple_lr.py
# Simple Linear Regression
# Modified by Joao Gabano from Saidmadhu 2017.
# Date: 2019-03-01
# About: Examples on How to pickle the python object
from math import pow

def coefficients(x_readings, y_readings):
    """
    Calculating the simple linear regression coefficients (B0, B1)
    :param x_readings:
    :param y_readings:
    :return:
    """
    # Coefficient B1 = covariance of x_readings and y_readings divided by variance of x_readings
    # Directly calling the implemented covariance and the variance functions
    # To calculate the coefficient B1
    b1 = calCovariance(x_readings, y_readings) / float(calVariance(x_readings))
 
    # Coefficient B0 = mean of y_readings - ( B1 * the mean of the x_readings )
    b0 = calMean(y_readings) - (b1 * calMean(x_readings))
    return b0, b1

def calCovariance(readings_1, readings_2):
    """
    Calculate the covariance between two different list of readings
    :param readings_1:
    :param readings_2:
    :return:
    """
    readings_1_mean = calMean(readings_1)
    readings_2_mean = calMean(readings_2)
    readings_size = len(readings_1)
    covariance = 0.0
    for i in xrange(0, readings_size):
        covariance += (readings_1[i] - readings_1_mean) * (readings_2[i] - readings_2_mean)
    return covariance / float(readings_size - 1)

def calVariance(readings):
    """
    Calculating the variance of the readings
    :param readings:
    :return:
    """
 
    # To calculate the variance we need the mean value
    # Calculating the mean value from the calMean function
    readings_mean = calMean(readings)
    # mean difference squared readings
    mean_difference_squared_readings = [pow((reading - readings_mean), 2) for reading in readings]
    variance = sum(mean_difference_squared_readings)
    return variance / float(len(readings) - 1)

def calMean(readings):
    """
    Function to calculate the mean value of the input readings
    :param readings:
    :return:
    """
    readings_total = sum(readings)
    number_of_readings = len(readings)
    mean = readings_total / float(number_of_readings)
    return mean
