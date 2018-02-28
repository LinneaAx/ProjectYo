import numpy as np
from sklearn.svm import LinearSVC
from sklearn.externals import joblib


#takes a np.savez file and uses it as input. Will add option to change the parameters of the SVM, generate several models, generate output model file names that correspond to the parameters and model type.  
def train_model(input_file): 
    filz = np.load(input_file)    
    x = filz['x']
    y = filz['y']

    clf = LinearSVC()
    clf.fit(x, y)
    
    joblib.dump(clf,input_file+'.model.pkl')
    
if __name__ == '__main__':
    train_model('output.txt.npz')
