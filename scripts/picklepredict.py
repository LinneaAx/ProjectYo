#!/usr/bin/env python3
import sys
import os
import developing_parse_code
import train_my_model
import predict_with_my_model
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import pickle

np.set_printoptions(threshold=np.nan)

#take a fasta input file, create windows using window from parse_code, make if binary using aa-coder from parse_code, load model using predict with my model, make it back into topologies, print out id, seq, top as fasta + topology

def input_predict(input_file, model='../generated_models/pickle/ws_59_alpha_beta_globular_sp_4state.txt_split_output.txt.npz.model.pkl'):
    file_handle = open(input_file, 'r')
    
    seq_ids = []
    seq = []    
    for line in file_handle:
        if line.startswith('>'):
            seq_ids.append(line.strip())
        else:
            seq.append(line.strip()) 
    file_handle_out = open(seq_ids[0]+'prediction_result', 'w')
    with open(model, 'rb') as pickle_file:
        clf = pickle.load(pickle_file)
        
    for i in range(len(seq_ids)):
        window = developing_parse_code.window(seq[i], 59)
        binary_word = developing_parse_code.aa_coder(window, 59)
        
        
        pred_result = []
        pred_result = clf.predict(binary_word)
        decoded = developing_parse_code.decoder(pred_result)
        strdecoded =''.join(decoded)
   
        file_handle_out.write(seq_ids[i]) #id_seq[i]
        file_handle_out.write('\n')
        file_handle_out.write(seq[i]) #seq[i]
        file_handle_out.write('\n')
        file_handle_out.write(strdecoded) 
        file_handle_out.write('\n')
    file_handle.close()
    file_handle_out.close()
    
if __name__ == '__main__':
    #input_fasta = sys.argv[1]
    #if len(sys.argv) >2:
    #    model = sys.argv[2]
    input_predict('../testdata/fasta.fasta')
