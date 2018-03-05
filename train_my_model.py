import parse_code
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score

#takes a np.savez file and uses it as input. Will add option to change the parameters of the SVM, generate several models, generate output model file names that correspond to the parameters and model type.  
def train_model(input_file): 
    filz = np.load(input_file)    
    x = filz['x']
    y = filz['y']

    clf = LinearSVC()
    #clf.fit(x, y)
    
    cross_score = cross_val_score(clf, x, y, cv = 10, verbose=True)
    #clf.get_params() #prints out the parameters the model builds on, useful later?    
    cross_score_average = np.average(cross_score)
    
    
    print(cross_score)
    file_handle = open('val_output.txt', 'w')
    file_handle.write(input_file, cross_score_average) # why doesnt this work??
    
    joblib.dump(clf,input_file+'.model.pkl')
    
if __name__ == '__main__':
    train_model('output.txt.npz')
    


