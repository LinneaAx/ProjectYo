import matplotlib
matplotlib.use('Agg')
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import confusion_plot
import matplotlib.pyplot as plt

#import data from np.savez 
def vectors_savez(input_file):
    global x, y
    filz = np.load(input_file)    
    x = filz['x'] #whatever name you have used to save the vectors 
    y = filz['y']

    return(x, y)

#use sklearn train_test_split to generate train test data split
x, y = vectors_savez('../splitoutput/ws_59_alpha_beta_globular_sp_4state.txt_split_output.txt.npz')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30)

#decision tree classifier

clf = DecisionTreeClassifier()
tree_cross_score = cross_val_score(clf, x_train, y_train, cv = 10, verbose=True)
print('Decision tree cross validation done...')
tree_score_mean = tree_cross_score.mean()
clf.fit(x_train, y_train)
print('Decision tree training done...')
tree_y_predicted = clf.predict(x_test)
labels = [1, 2, 3, 4]
target_names = ['G', 'M', 'I', 'O']
tree_classreport = classification_report(y_test, tree_y_predicted, labels = labels, target_names = target_names)
tree_confusionm = confusion_matrix(y_test, tree_y_predicted)
tree_mcc = matthews_corrcoef(y_test, tree_y_predicted)


plt.figure()
confusion_plot.plot_confusion_matrix(tree_confusionm, classes=target_names, normalize=True,
                      title='Normalized confusion matrix')
plt.savefig('../outputfiles/tree_confusion_unbalanced2.png')
plt.tight_layout
()
plt.close()


#randomforestclassifier

clf = RandomForestClassifier()
random_cross_score = cross_val_score(clf, x_train, y_train, cv = 10, verbose=True)
print('Random forest cross validation done...')
random_score_mean = random_cross_score.mean()
clf.fit(x_train, y_train)
print('Random forest training done...')

random_y_predicted = clf.predict(x_test)
random_classreport = classification_report(y_test, random_y_predicted, labels = labels, target_names = target_names)
random_confusionm = confusion_matrix(y_test, random_y_predicted)
random_mcc = matthews_corrcoef(y_test, random_y_predicted)

plt.figure()
confusion_plot.plot_confusion_matrix(random_confusionm, classes=target_names, normalize=True,
                      title='Normalized confusion matrix')
plt.savefig('../outputfiles/random_confusion_unbalanced2.png')
plt.tight_layout()
plt.close()

#Training and testing the different classifiers LinearSVC, decisiontree and randomforest
#SVM classifier
 
clf = LinearSVC()
svm_cross_score = cross_val_score(clf, x_train, y_train, cv = 10, verbose=True)
print('SVM cross validation done...')
svm_cross_mean = svm_cross_score.mean()
clf.fit(x_train, y_train)
print('SVM training done...')
svm_y_predicted = clf.predict(x_test)
print(svm_y_predicted)
svm_classreport = classification_report(y_test, svm_y_predicted, labels = labels, target_names = target_names)
svm_confusionm = confusion_matrix(y_test, svm_y_predicted)
svm_mcc = matthews_corrcoef(y_test, svm_y_predicted)

plt.figure()
confusion_plot.plot_confusion_matrix(svm_confusionm, classes=target_names, normalize=True,
                      title='Normalized confusion matrix')
plt.savefig('../outputfiles/svm_confusion_unbalanced2.png')
plt.tight_layout()
plt.close()


with open ('../outputfiles/results_svm_tree_random_unbalanced2.txt', 'w') as f:
    f.write('Cross-validation scores for LinearSVC: ' + str(svm_cross_mean)+ '\n')
    f.write('Cross-validation scores for DecisionTreeClassifier: '+ str(tree_score_mean)+ '\n')
    f.write('Cross-validation scores for RandomForestClassifier: '+ str(random_score_mean)+ '\n')
    f.write('Matthews correlation coefficient (MCC) SVM: ' + str(svm_mcc) + '\n')
    f.write('Matthews correlation coefficient (MCC) DecisionTreeClassifier: ' + str(tree_mcc) + '\n')
    f.write('Matthews correlation coefficient (MCC) RandomForestClassifier: ' + str(random_mcc) + '\n')            
    f.write('Classification report SVM: ' + '\n' + str(svm_classreport) + '\n')
    f.write('Confusion matrix SVM: ' + '\n' + str(svm_confusionm) + '\n')
    f.write('Classification report DecisionTreeClassifier: ' + '\n' + str(tree_classreport) + '\n')
    f.write('Confusion matrix DecisionTreeClassifier: ' + '\n' + str(tree_confusionm) + '\n')
    f.write('Classification report RandomForestClassifier: ' + '\n' + str(random_classreport) + '\n')
    f.write('Confusion matrix RandomForestClassifier: ' + '\n' + str(random_confusionm) + '\n')
    f.close()


if __name__ == '__main__':
    vectors_savez('../splitoutput/ws_59_alpha_beta_globular_sp_4state.txt_split_output.txt.npz')
    
