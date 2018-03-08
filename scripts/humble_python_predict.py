#!/usr/bin/env python3
import sys
import os
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
    seq = fasta[1]
    
    binary_word = parse_code.aa_top_coder(seq)
    print(binary_word)
    clf = joblib.load(model)
    pred_result = []
    pred_result = clf.predict(binary_word)
    print(pred_result)
    
    decoded = parse_code.decoder(pred_result)
    print(decoded)
    
    file_handle_out = open('prediction_result_from'+input_file, 'w')
    file_handle_out.write(id_seq)
    file_handle_out.write('\n')
    file_handle_out.write(seq)
    file_handle_out.write('\n')
    file_handle_out.write(decoded)

file_handle.close()
file_handle_out.close()
    
    
