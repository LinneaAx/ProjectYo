#!/usr/bin/env python3
import sys
import os
import numpy as np

BASE_PATH = "../splitoutput/"

top_dic = { 'G':1, 'M':2, 'I':3, 'O':4 }

decode_top_dic = { 1:'G', 2:'M', 3:'I', 4:'O' }

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

def parseprot(file_input):
    filehandle = open(file_input, 'r')
    filehandle = filehandle.read().splitlines()
    proteinseq = [filehandle[i] for i in range(1, len(filehandle), 3)]
    return(proteinseq)
    
def parsetop(file_input):
    filehandle = open(file_input, 'r')
    filehandle = filehandle.read().splitlines()
    topology = [filehandle[i] for i in range(2, len(filehandle), 3)]
    return(topology)    
    
    
def window(file_input, windowsize):
    ws = int(windowsize)
    n = int(ws/2)
   
    protteseq = parseprot(file_input)
    windowz = []
    for protseq in protteseq:
        protseq = ((n)*'0')+protseq+((n)*'0')
        for i in range(0, len(protseq)):
            if i+(ws) > len(protseq):
                break
            temp = protseq[i:i+(ws)]
            windowz.append(temp)
    return(windowz)
    
def aa_top_coder(file_input, windowsize, dicaa=aa_dic, dictop=top_dic):
    
    binary_word = []
    windows = window(file_input, windowsize)
    for elements in windows:
        temp = []
        for characters in elements:
            binary = dicaa[characters]
            temp.append(binary)
        temp = [characters for elements in temp for characters in elements]
        binary_word.append(temp)
    binary_word = np.array(binary_word)
        
    coded_label = []
    topology = parsetop(file_input)
    for top in topology:
        labelz = [dictop[letter] for letter in top] 
        coded_label.extend(labelz)   
    coded_label = np.array(coded_label)
    
    outfile ='ws_'+str(windowsize)+'_'+file_input+'_output.txt'
    np.savez( os.path.join(BASE_PATH, outfile), x=binary_word, y=coded_label)
    print('coding done')
    return(binary_word, coded_label)

top_top_dic = { 1:'G', 2:'M', 3:'I', 4:'O' }

def decoder(sequence, dictionary=top_top_dic):
    new_name = []
    for elements in sequence:
        newname = [dictionary[elements]]
        new_name.extend(newname)
    return(new_name)
    
    
if __name__ == '__main__':

    aa_top_coder('alpha_beta_globular_sp_4state.txt_split', '3', aa_dic, top_dic)
    #input_file = sys.argv[1]
    
    #if len(sys.argv) > 2:
    #kernel = sys.argv[2]
    #somethingelse = sys.argv[3]
  
    
    
