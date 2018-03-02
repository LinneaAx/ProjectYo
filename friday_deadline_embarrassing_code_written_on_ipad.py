from sklearn import svm
import numpy as np
from sklearn.svm import LinearSVC


#######################################################################
# Open file and split into lists
#######################################################################

filehandle = open('alpha_beta_globular_sp_4state_mini.txt', 'r')
file_input = filehandle.read().splitlines()


proteinname = [file_input[i] for i in range(0, len(file_input), 3)]
proteinseq = [file_input[i] for i in range(1, len(file_input), 3)]
topology = [file_input[i] for i in range(2, len(file_input), 3)]

#######################################################################
# Select window size, for an odd number windowsize ! Do I need to add exception?  
#######################################################################

ws = int(3)
n = int(ws/2)

########################################################################
# Fix the windows 
########################################################################

windowz = []
for protseq in proteinseq:
    protseq = ((n)*'0')+protseq+((n)*'0')
    for i in range(0, len(protseq)):
        if i+(ws) > len(protseq):
            break
        temp = protseq[i:i+(ws)]
        windowz.append(temp)
print(windowz)

########################################################################
# Map aa's to binary code
########################################################################

binary_word = []
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
print(topology)

for elements in windowz:
    temp = []
    for characters in elements:
        binary = aa_dic[characters]
        temp.append(binary)
    temp = [characters for elements in temp for characters in elements]
    binary_word.append(temp)

######################################################################
# Map labels to numbers
######################################################################

binary_label = []
top_binary_dic = { 'G':1, 'M':2, 'I':3, 'O':4 }

for top in topology:
    print(topology)
    labelz = [top_binary_dic[letter] for letter in top] 
    binary_label.extend(labelz)

print(binary_label)


######################################################################
# Train SVM 
######################################################################


x = np.array(binary_word)
y = np.array(binary_label)

clf = LinearSVC()
clf.fit(x, y)

#joblib.dump(clf,'model.pkl')


################
# predict with model
#################

sequence = 'ASSTYRGT'

predict_window = []
for protseq in sequence:
    protseq = ((n)*'0')+protseq+((n)*'0')
    for i in range(0, len(protseq)):
        if i+(ws) > len(protseq):
            break
        temp = protseq[i:i+(ws)]
        predict_window.append(temp)

binary_word = []
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

for elements in predict_window:
    temp = []
    for characters in elements:
        binary = aa_dic[characters]
        temp.append(binary)
    temp = [characters for elements in temp for characters in elements]
    binary_word.append(temp)
z =np.array(binary_word)

result = clf.predict(z)

top_top_dic = { 1:'G', 2:'M', 3:'I', 4:'O' }

pred_topology = []
for elements in resultat:
    newname = [top_top_dic[elements]]
    pred_topology.extend(newname)

print(sequence, pred_topology)
