# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values
#Taking care of missing data
from sklearn.impute import SimpleImputer
imputer   = SimpleImputer(missing_values = np.nan, strategy = 'mean', verbose = 0)
X[:, 1:3] = imputer.fit_transform(X[:,1:3])

