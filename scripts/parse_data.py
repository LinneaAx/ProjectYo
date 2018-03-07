def parseprot(file_input):
    filehandle = open(file_input, 'r')
    filehandle_out = open(file_input+'_split', 'w')
    data = list(filehandle)
    idlist = data[0::3]
    seqlist = data[1::3]
    topolist = data[2::3]
    
    counter = 0
    gcounter = 0
    for ids in range(len(topolist)):
        if topolist[ids].startswith('I') or topolist[ids].startswith('M') or topolist[ids].startswith('O')  == True:
            filehandle_out.write(idlist[ids])
            filehandle_out.write(seqlist[ids])
            filehandle_out.write(topolist[ids])
            counter += 1
            
        elif topolist[ids].startswith('G') == True:
            if gcounter <313:
                filehandle_out.write(idlist[ids])
                filehandle_out.write(seqlist[ids])
                filehandle_out.write(topolist[ids])
                gcounter += 1
    filehandle_out.close()
    print(counter, gcounter, 'done')
    return('Finished splitting yo data')
    
if __name__ == '__main__':
    parseprot('alpha_beta_globular_sp_4state.txt')
