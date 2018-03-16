#Changed in an attempt to make a bash script that predicts by taking in seq id, blasting etc. Not finished. 


import sys

def save_fastas(input_file):
    filehandle = open(input_file, 'r')
    data = filehandle.read().splitlines()
    idlist = data[0::2]
    seqlist = data[1::2]
    
    
    for j in range(len(idlist)):        
        with open ('../fastas/to_predict/' + idlist[j] + '.fasta', 'w') as f:
            f.write(str(idlist[j]) + '\n')
            f.write(str(seqlist[j]) + '\n')
            f.close()
        
if __name__ == '__main__':
    input_file = sys.argv[1]
    save_fastas(input_file)
    #save_fastas('../../data/alpha_beta_globular_sp_4state.txt_split')
