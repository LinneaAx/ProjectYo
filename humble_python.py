#python script for parsing, training and optimizing for different window sizes 
import parse_code
import train_my_model
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score


def create_those_windows(input_data):
    file_handle = open('3_33_val_output.txt', 'w')
    for windowsize in range(3, 34, 2):
        X, Y = parse_code.aa_top_coder(input_data, windowsize) #files saved in test
        clf = LinearSVC()
        clf.fit(X, Y)
        
        cross_score = cross_val_score(clf, X, Y, cv = 10, verbose=True, n_jobs=-1)
        #params = clf.get_params() #prints out the parameters the model builds on, useful later?
        cross_score_average = np.average(cross_score)
    
        joblib.dump(clf,str(windowsize)+'_'+input_data+'_model.pkl')
        print('Model created of windowsize:', windowsize)
        file_handle.write(str(windowsize))
        file_handle.write(input_data) # why doesnt this work??
        #file_handle.write(str(params))
        file_handle.write(str(cross_score_average))
        file_handle.write('\n')
    file_handle.close()        
        
if __name__ == '__main__':
    create_those_windows('alpha_beta_globular_sp_4state.txt_split')
