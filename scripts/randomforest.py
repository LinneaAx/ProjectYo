import numpy as np
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

#import data from np.savez 
def vectors_savez(input_file):
    filz = np.load(input_file)    
    x = filz['x'] #whatever name you have used to save the vectors 
    y = filz['y']

    return(x, y)

#use sklearn train_test_split to generate train test data split
x, y = vectors_savez('../splitoutput/ws_3_alpha_beta_globular_sp_4state.txt_split_output.txt.npz')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.10)

#Training and testing the different classifyers LinearSVC, decisiontree and randomforest
#SVM classifier
 
clf = LinearSVC()
svm_cross_score = cross_val_score(clf, x, y, cv = 10, verbose=True)
print('SVM cross validation done...')
svm_cross_mean = svm_cross_score.mean()
clf.fit(x_train, y_train)
print('SVM training done...')
svm_y_predicted = clf.predict(x_test)
svm_classreport = classification_report(y_test, svm_y_predicted, labels = ['1', '2', '3', '4'])
svm_confusionm = confusion_matrix(y_test, svm_y_predicted, labels = ['1', '2', '3', '4'])


#decision tree classifier

clf = DecisionTreeClassifier(max_depth=None, min_samples_split=2, random_state=0)
tree_cross_score = cross_val_score(clf, x, y, cv = 10, verbose=True)
print('Decision tree cross validation done...')
tree_score_mean = tree_cross_score.mean()
clf.fit(x_train, y_train)
print('Decision tree training done...')
tree_y_predicted = clf.predict(x_test)
tree_classreport = classification_report(y_test, tree_y_predicted, labels = ['1', '2', '3', '4'])
tree_confusionm = confusion_matrix(y_test, tree_y_predicted, labels = ['1', '2', '3', '4'])


#randomforestclassifier

clf = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)
random_cross_score = cross_val_score(clf, x, y, cv = 10, verbose=True)
print('Random forest cross validation done...')
random_score_mean = random_cross_score.mean()
clf.fit(x_train, y_train)
print('Random forest training done...')
random_y_predicted = clf.predict(x_test)
random_classreport = classification_report(y_test, random_y_predicted, labels = ['1', '2', '3', '4'])
random_confusionm = confusion_matrix(y_test, random_y_predicted, labels = ['1', '2', '3', '4'])


with open ('../outputfiles/results_svm_tree_random.txt', 'w') as f:
    f.write('Cross-validation scores for LinearSVC: ' + str(svm_cross_mean)+ '\n')
    f.write('Cross-validation scores for DecisionTreeClassifier: '+ str(tree_score_mean)+ '\n')
    f.write('Cross-validation scores for RandomForestClassifier: '+ str(random_score_mean)+ '\n')
    f.write('Classification report SVM: ' + '\n' + str(svm_classreport) + '\n')
    f.write('Confusion matrix SVM: ' + '\n' + str(svm_confusionm) + '\n')
    f.write('Classification report DecisionTreeClassifier: ' + '\n' + str(tree_classreport) + '\n')
    f.write('Confusion matrix DecisionTreeClassifier: ' + '\n' + str(tree_confusionm) + '\n')
    f.write('Classification report RandomForestClassifier: ' + '\n' + str(random_classreport) + '\n')
    f.write('Confusion matrix RandomForestClassifier: ' + '\n' + str(random_confusionm) + '\n')
f.close()


if __name__ == '__main__':
    vectors_savez('../splitoutput/ws_3_alpha_beta_globular_sp_4state.txt_split_output.txt.npz')
    
