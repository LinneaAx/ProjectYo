#!/usr/bin/env python3
import sys
import os
import numpy as np

np.set_printoptions(threshold=np.nan)

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

def parseprotpredict(file_input):
    filehandle = open(file_input, 'r')
    filehandle = filehandle.read().splitlines()
    proteinseq = [filehandle[i] for i in range(1, len(filehandle), 2)]
    return(proteinseqpred)


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
    
    
def window(datainput, windowsize):
    ws = int(windowsize)
    n = int(ws/2)
   
    windowz = []
    protseq = str(data_input)
    protseq = ((n)*'0')+protseq+((n)*'0')
    for i in range(0, len(protseq)):
        if i+(ws) > len(protseq):
            break
        temp = protseq[i:i+(ws)]
        windowz.append(temp)
    return(windowz)
    
def aa_coder(file_input, windowsize, aa_dic=aa_dic):
    
    binary_word = []
    for elements in file_input:
        temp = []
        print(elements)
        for characters in elements:
            print(characters)
            binary = aa_dic[characters]
            temp.extend(binary)
        #temp = [characters for elements in temp for characters in elements]
        binary_word.append(temp)
    binary_word = np.array(binary_word)
    return(binary_word)
    
def top_coder(file_input, windowsize, top_dic=top_dic):     
    coded_label = []
    topology = parsetop(file_input)
    for top in topology:
        labelz = [top_dic[letter] for letter in top] 
        coded_label.extend(labelz)   
    coded_label = np.array(coded_label)
    
    outfile ='ws_'+str(windowsize)+'_'+file_input+'_output.txt'
    np.savez( os.path.join(BASE_PATH, outfile), x=aa_coder(file_input, windowsize), y=coded_label)
    print('coding done')
    return(coded_label)

top_top_dic = { 1:'G', 2:'M', 3:'I', 4:'O' }

def decoder(sequence, dictionary=top_top_dic):
    new_name = []
    for elements in sequence:
        newname = [dictionary[elements]]
        new_name.extend(newname)
    return(new_name)
    
    
if __name__ == '__main__':
    
    top_coder('../data/alpha_beta_globular_sp_4state_mini.txt', '3', top_dic)
    #input_file = sys.argv[1]
    
    #if len(sys.argv) > 2:
    #kernel = sys.argv[2]
    #somethingelse = sys.argv[3]
  
    
    
