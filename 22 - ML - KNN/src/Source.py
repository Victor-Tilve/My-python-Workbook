'''
Created on 2/02/2021

@author: VATS
'''
import numpy as np
from collections import Counter 

    #It cpulb be in a utility file
def euclidean_distance(x1,x2):
    return np.sqrt(np.sum(x1 - x2)**2)
        

class KNN(object):
    '''
    classdocs
    '''

    def __init__(self, k = 3):
        self.k = k
    
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
    
    def predict(self, X):
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)
    #Helper Method
    def _predict(self, x):
        #Compute distances
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        #get k nearest sample, label
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices] #List comprenhension
        #Majority vote, most common class  label
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]