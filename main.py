# -*- coding: utf-8 -*-
"""for分作ってみる.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P935spSkw3fPp0nXqh5z9-ZFptlhBmJ3
"""

import numpy as np

import pandas as pd

import yfinance as yf

import matplotlib.pyplot as plt

aapl = yf.Ticker('AAPL')

aapl.history()

