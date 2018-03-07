import parse_code
import train_my_model
import predict_with_my_model
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score

#take a fasta input file, make if binary using parse_code, load model using predict with my model, make it back into topologies, print out id, seq, top as fasta + topology

def input_predict(input_file, model):
    file_handle = open(input_file, 'r')
    fasta = list(file_handle)
    id_seq = fasta[0]
    
    binary_word = parse_code.aa_top_coder(input_file)[0]
    print(binary_word)
    clf = joblib.load(model)
    pred_result = []
    pred_result = clf.predict(binary_word)
    print(pred_result)
    
    
    
