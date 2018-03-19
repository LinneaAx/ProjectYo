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
import parse_code
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score

def make_binary_file(input_file, windowsize):
    parse_code.top_coder(input_file, windowsize)

#import data from np.savez 
def predict50(input_file, windowsize, model):
    global x, y
    filz = np.load('proteins50_data.npz')    
    x = filz['x'] #whatever name you have used to save the vectors 
    y = filz['y']
    
    clf = joblib.load(model)
    coded = clf.predict(x)
    svm_y_predicted = parse_code.decoder(coded)

    svm_y_predicted = clf.predict(x)
    print(svm_y_predicted)
    labels = [1, 2, 3, 4]
    target_names = ['G', 'M', 'I', 'O']

    svm_classreport = classification_report(y, svm_y_predicted, labels = labels, target_names = target_names)
    svm_confusionm = confusion_matrix(y, svm_y_predicted)
    svm_mcc = matthews_corrcoef(y, svm_y_predicted)
    svm_acc = accuracy_score(y, svm_y_predicted)
    print(svm_acc)
    print(svm_mcc)
    plt.figure()
    confusion_plot.plot_confusion_matrix(svm_confusionm, classes=target_names, normalize=True,
                      title='Normalized confusion matrix prediction of 50 proteins')
    plt.savefig('../outputfiles/svm_confusion50.png')
    plt.tight_layout()
    plt.close()

#make_binary_file('../data/proteins50.txt', 59)
predict50('proteins50.txt', 59, '../generated_models/59_alpha_beta_globular_sp_4state.txt_split_model.pkl')

