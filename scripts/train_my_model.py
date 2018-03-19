import numpy as np
import pickle
import sys
from sklearn.svm import LinearSVC
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

#takes a np.savez file and uses it as input. Will add option to change the parameters of the SVM, generate several models, generate output model file names that correspond to the parameters and model type.  
def train_model(input_file): 
    filz = np.load(input_file)    
    x = filz['x']
    y = filz['y']

    clf = LinearSVC()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30)
    svm_cross_score = cross_val_score(clf, x, y, cv = 10, verbose=True, n_jobs = -1)
    svm_cross_mean = svm_cross_score.mean()
    print('SVM cross validation done...')
    
    clf.fit(x_train, y_train)
    print('SVM training done...')
    svm_y_predicted = clf.predict(x_test)
    labels = [1, 2, 3, 4]
    target_names = ['G', 'M', 'I', 'O']
    svm_classreport = classification_report(y_test, svm_y_predicted, labels = labels, target_names = target_names)
    svm_confusionm = confusion_matrix(y_test, svm_y_predicted, labels = labels)
    svm_mcc = matthews_corrcoef(y_test, svm_y_predicted)
    
    params = clf.get_params()
    
    
    with open ('../../generated_models/pickle' + str(input_file) + '.model.pkl', 'rb') as q:
        pickle.dump(clf, q)
    
    with open ('../../outputfiles/poopws_optimization_results.txt', 'a') as f:
        f.write(input_file + '\n') 
        #f.write(str(params) + ' ')
        f.write('Cross-validation scores for LinearSVC: ' + str(svm_cross_mean) + '\n')
        f.write('Matthews correlation coefficient (MCC) SVM: ' + str(svm_mcc) + '\n')
        f.write('Classification report SVM: ' + '\n' + str(svm_classreport) + '\n')
        f.write('Confusion matrix SVM: ' + '\n' + str(svm_confusionm) + '\n')
        f.close()
    with open ('../../outputfiles/ws_mcc_results.txt', 'a') as e:
        e.write(input_file + ' ')
        e.write('Matthews correlation coefficient (MCC) SVM: ' + str(svm_mcc) + '\n')
        e.close()

if __name__ == '__main__':
    input_file = sys.argv[1]
    train_model(input_file)
    
    #train_model('ws_3_alpha_beta_globular_sp_4state.txt_split_output.txt.npz')
    


