#Creates fasta file for PSI-Blast run, sequence name and sequence

import pandas as pan

filehandle = 'alpha_beta_globular_sp_4state.txt_split'

raw_data = pan.read_csv(filehandle, header=None)
drop_list = []

for a in range(len(raw_data)):
    if (a+1) %3 == 0:
        drop_list.extend([a])

raw_data.drop(raw_data.index[drop_list], inplace=True)
raw_data.reset_index(drop = True, inplace = True)

raw_data.to_csv(filehandle+'.fasta', header=None, index=None)
