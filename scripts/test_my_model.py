import numpy as np
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score


cross_score = cross_val_score(clf, X, cv = 10, verbose=True)
#kf = KFold(n_splits=10)

inputmodel.get_params() #prints out the parameters the model builds on


#parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
#svc = svm.SVC()
#clf = GridSearchCV(svc, parameters)
#clf.fit(X, Y)
#sorted(clf.cv_results_.keys())
