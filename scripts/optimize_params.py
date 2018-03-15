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


def optimize_params(input_file): 
    filz = np.load(input_file)    
    x = filz['x']
    y = filz['y']
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30)
    
    svc = LinearSVC()
    parameters = {'C':[0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1]}
    clf = GridSearchCV(svc, parameters)
    clf.fit(x_train, y_train)
    res = pd.DataFrame(clf.cv_results_)

    res.to_csv('../outputfiles/optimize_c.csv', sep='\t', encoding='UTF-8')
    print('done with first function')
    
def valid_curve(input_file):
    filz = np.load(input_file)    
    x = filz['x']
    y = filz['y']
        
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
    plt.ylim(0.0, 1.1)
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
    
    
    
if __name__ == '__main__':
    optimize_params('../splitoutput/ws_59_alpha_beta_globular_sp_4state.txt_split_output.txt.npz')
    valid_curve('../splitoutput/ws_59_alpha_beta_globular_sp_4state.txt_split_output.txt.npz') 
