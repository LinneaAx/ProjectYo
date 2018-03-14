def save_fastas(input_file):
    filehandle = open(input_file, 'r')
    data = filehandle.read().splitlines()
    idlist = data[0::3]
    seqlist = data[1::3]
    
    
    for j in range(len(idlist)):        
        with open ('../fastas/' + idlist[j] + '.fasta', 'w') as f:
            f.write(str(idlist[j]) + '\n')
            f.write(str(seqlist[j]) + '\n')
            f.close()
        
save_fastas('../../data/alpha_beta_globular_sp_4state.txt_split')
