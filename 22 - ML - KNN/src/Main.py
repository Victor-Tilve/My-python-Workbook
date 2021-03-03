'''
Created on 2/02/2021

@author: VATS
URL: https://www.youtube.com/watch?list=PLqnslRFeH2Upcrywf-u2etjdxxkL8nl7E&v=ngLyX54e1LU
'''

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

cmap = ListedColormap(['#FF0000','#00FF00','#0000FF'])


import Source

iris = datasets.load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X ,y , test_size = 0.2, random_state = 1234)


if __name__ == '__main__':
    
    '''print(X_train.shape)
    print(X_train[0])
    print(y_train.shape)
    print(y_train)
    
    plt.figure()
    plt.scatter(X[:,0],X[:,1],c = y, cmap = cmap, edgecolors= 'k', s = 20)
    plt.show()'''
    
    '''a = [1,1,1,2,2,3,4,5,6]
    from collections import Counter
    most_common = Counter(a).most_common(1)
    print(most_common[0][0])
    '''
    from Source import KNN
    clf = KNN(k = 3) 
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    
    acc = np.sum(predictions == y_test) / len(y_test)       # accuarety
    print(predictions)
    print(y_test)
    print(acc)
    print(np.sum(predictions == y_test))
    print(len(y_test))
    