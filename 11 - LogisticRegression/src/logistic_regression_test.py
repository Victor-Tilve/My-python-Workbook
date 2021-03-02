'''
Created on 26/02/2021

@author: vtilve
'''

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

from logistic_regression import LogisticRegression

bc = datasets.load_breast_cancer()
X, y = bc.data, bc.target

X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size = 0.2, random_state = 1234)

def accuary (y_true, y_pred):
    accuary = np.sum(y_true == y_true) / len(y_true)
    return accuary

regresor = LogisticRegression(lr = 0.0001, n_iters = 1000)
regresor.fit(X_train, y_train)
prediction = regresor.predict(X_test)

print(f'LR classification accuary: {accuary(y_test, prediction)}')
print('LR classification accuary:', accuary(y_test, prediction))
print('y_test: ',y_test)
print('prediction: ',prediction)
print(np.unique(prediction))