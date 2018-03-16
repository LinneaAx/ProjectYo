import numpy as np
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import validation_curve

def valid_curve():
   # filz = np.load(input_file)    
   # x = filz['x']
   # y = filz['y']
    x = ('a', 'b', 'c')
    y = (1, 2, 3)
    x = np.array(x)
    y = np.array(y)    
    param_range = np.logspace(-3, 2, num=10)
    train_scores, test_scores = validation_curve(
    LinearSVC(), x, y, param_name="C", param_range=param_range,
    cv=3, scoring="accuracy", n_jobs=1)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    
    plt.title("Validation Curve with SVM")
    plt.xlabel("$\C$")
    plt.ylabel("Score")
    lw = 2
    plt.semilogx(param_range, train_scores_mean, label="Training score",
                 color="darkorange", lw=lw)
    plt.fill_between(param_range, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.2,
                     color="darkorange", lw=lw)
    plt.semilogx(param_range, test_scores_mean, label="Cross-validation score",
                 color="navy", lw=lw)
    plt.fill_between(param_range, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.2,
                     color="navy", lw=lw)
    plt.legend(loc="best")
    plt.show()
    plt.savefig('figure.png')

valid_curve()
