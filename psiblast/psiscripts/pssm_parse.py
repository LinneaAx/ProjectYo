import sys 
sys.path.insert(0,"../../codes")
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
import pickle
from sklearn.svm import LinearSVC

def extract_info(dataset):
    filehandle = open(dataset, 'r')
    data = filehandle.read().splitlines()
    idlist = data[0::3]
    seqlist = data[1::3]
    topolist = data[2::3]
    print(len(idlist))
    return(idlist, seqlist, topolist)


def train_pssm(idlist, topolist, window):
    '''Takes pssms from X_train and trains and saves model'''    
    
    pssm_list_train = []    
    for ids in idlist:
        pssm = '../pssms/' + ids + '.fasta' #location of your pssms
        pssm_list_train.append(np.genfromtxt(pssm, skip_header=3, skip_footer=5, usecols=range(22,42)))
        
    X_train = pssm_list_train    
    X_train_changed, array_numbering = extract_pssms(X_train, window)
    
    
    top_dic = { 'G':1, 'M':2, 'I':3, 'O':4 }
    Y_train_changed = []
    for proteins in topolist:    
        for topologies in proteins:
            y = top_dic[topologies]
            Y_train_changed.append(y)
    clf = LinearSVC()
    clf.fit(X_train_changed, Y_train_changed)
    filename = 'pssm_model.sav'
    pickle.dump(clf, open(filename, 'wb'))
    

def extract_pssms(pssm_list, window):
    padding = window // 2
    arrays = []
    numbering = []
    
    for number, matrix in enumerate(pssm_list):
        length = len(matrix)
        training = np.zeros((length, window, 20))
        decimal_pssm = matrix / 100
        pad_matrix = np.vstack([np.zeros((padding, 20)), decimal_pssm, np.zeros((padding, 20))])
        for aa in range(length):
            training[aa] = pad_matrix[aa:aa + window]
            numbering.append(number)
        arrays.append(training.reshape(length, window *20))
    return np.vstack(arrays), numbering
            
           
if __name__ == '__main__':  
    idlist, seqlist, topolist = extract_info('../../data/pssm_data.txt_split')
    train_pssm(idlist, topolist, 3) #called with window size 3
