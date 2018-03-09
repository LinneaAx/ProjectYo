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

np.set_printoptions(threshold=np.nan)

aa_dic = {  'A':[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
			'C':[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			'D':[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
			'E':[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
			'F':[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
			'G':[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
			'H':[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0], 
			'I':[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0], 
			'K':[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0], 
			'L':[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0], 
			'M':[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0], 
			'N':[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
 			'Q':[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
			'P':[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0], 
			'R':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0], 
			'S':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0], 
			'T':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0], 
			'V':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0], 
			'W':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], 
			'Y':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
			'0':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]} 


#take a fasta input file, make if binary using parse_code, load model using predict with my model, make it back into topologies, print out id, seq, top as fasta + topology

def input_predict(input_file, model):
    file_handle = open(input_file, 'r')
    fasta = file_handle.read().splitlines()
    id_seq = fasta[0] 
    seq = fasta[1] 
    
    binary_word = parse_code.aa_coder(input_file, 3)
    
    clf = joblib.load(model)
    pred_result = []
    pred_result = clf.predict(binary_word)
    
    decoded = parse_code.decoder(pred_result)
    strdecoded =''.join(decoded)
    
    
    file_handle_out = open('prediction_result_from'+input_file, 'w')
    file_handle_out.write(id_seq) 
    file_handle_out.write('\n')
    file_handle_out.write(seq) 
    file_handle_out.write('\n')
    file_handle_out.write(strdecoded) 

    file_handle.close()
    file_handle_out.close()
    
if __name__ == '__main__':
    input_predict('fasta.fasta', '../generated_models/3_alpha_beta_globular_sp_4state.txt_split_model.pkl')
