import numpy as np
from sklearn.svm import LinearSVC
from sklearn.externals import joblib

def predict_with_model(input_file, model):
    
    filz = np.load(input_file)    
    x = filz['x']
    y = filz['y']
    
    clf = joblib.load(model)
    pred_result = []
    pred_result = clf.predict(x,y)
    
if __name__ == '__main__':
    predict_with_model('output.txt.npz.model.pkl')
