import numpy as np
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

def optimize_params(input_file): 
    filz = np.load(input_file)    
    x = filz['x']
    y = filz['y']
    
    #x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30)
    
    svc = LinearSVC() #change maria!!!
    #parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10], 'gamma':[0.1, 0.5, 1]}
    parameters = {'C':[0.1, 1, 10, 20]}
    clf = GridSearchCV(svc, parameters)
    clf.fit(x_train, y_train)
    res = pd.DataFrame(clf.cv_results_)

    res.to_csv('../outputfiles/optimize_c.csv', sep='\t', encoding='UTF-8')
   
if __name__ == '__main__':
    optimize_params('../splitoutput/ws_3_alpha_beta_globular_sp_4state.txt_split_output.txt.npz')
