# -*- coding: utf-8 -*-
"""exercise.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H_EHN9mRUQDPmwqPTD23nmuoCWcaW6Mk

# Exercice
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gc

# Logic
unique_list = []

def check_uniqueness(lst):
    """
    Check if a list contains only unique values.
    Returns True only if all values in the list are unique, False otherwise
    """
    for x in lst:
      if x not in unique_list :
        unique_list.append(x)
    if (len(unique_list) == len(lst)):
      return True
    else:
      return False   
    pass

check_uniqueness([1,3,2])

check_uniqueness([1,3,2,3])

def smallest_difference(array):
  if not array:
    return []
  array.sort()
  min_diff = array[1] - array[0]
  for i in range(2, len(array)):

    min_diff = min(min_diff, (array[i] - array[i - 1]))
    result = []
  for i in range(1, len(array)):
    if array[i] - array[i - 1] == min_diff:
      result.append(min_diff)
    return result
  pass

smallest_difference([11,22,13,10])

from google.colab import drive
drive.mount('/content/drive')

prices = pd.read_csv('/content/drive/MyDrive/data.csv' , index_col = 'date', parse_dates =True)
test = pd.read_csv('/content/drive/MyDrive/output.csv' , index_col = 'date', parse_dates =True)

prices.columns = prices.columns.str.replace(' ', '')

prices.info()

def macd(prices, window_short=12, window_long=26):
    """
    Code a function that takes a DataFrame named prices and
    returns it's MACD (Moving Average Convergence Difference) as
    a DataFrame with same shape
    Assume simple moving average rather than exponential moving average
    The expected output is in the output.csv file
    """
    x = prices.SX5TIndex.rolling(12, min_periods=1).mean()

    y = prices.SX5TIndex.rolling(26, min_periods=1).mean()
    return x - y
    pass

prices['MACD'] = macd(prices)

"""The result obtained is similar to the output

"""

prices

"""to calculate the expected_shortfall , we must calculate the value_at_risk """

def value_at_risk(prices, level=.95):
  # Calculating VaR
	return prices.quantile(level, axis=0, interpolation='higher')

def expected_shortfall(prices, level=0.05):
	# Calculating VaR
  var = value_at_risk(prices, level)
  return prices[prices.lt(var, axis=1)].mean()

def expected_shortfall(prices, level=0.05):
  var = value_at_risk(prices, level)
  return returns[prices.lt(var, axis=1)].mean()
  pass

es = expected_shortfall(prices, level=0.05)

#we must delete the NA values
df = prices.pct_change().dropna()

def sortino_ratio(series, N,rf):
    mean = series.mean() * N -rf
    std_neg = series[series<0].std()*np.sqrt(N)
    return mean/std_neg

sortinos = df.apply(sortino_ratio, args=(15,0,), axis=0 )
sortinos

def visualize(prices, path):
    """
    Code a function that takes a DataFrame named prices and
    saves the plot to the given path
    """
    plt.figure(figsize=(15,10))
    plt.grid(True)
    plt.plot(prices['MACD'])
    plt.legend("Simple Average")
    plt.savefig(path)
    pass

result = visualize(prices , '/content/result.png')
