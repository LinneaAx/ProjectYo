def parseprot(file_input):
    filehandle = open(file_input, 'r')
    filehandle_out = open('../data/'+file_input+'_split_allrest', 'w')
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
            
            
        elif topolist[ids].startswith('G') == True:
                with open ('../data/' + file_input + '_split_allg', 'w') as q:
                    q.write(idlist[ids])
                    q.write(seqlist[ids])
                    q.write(topolist[ids])
                
    filehandle_out.close()
    q.close()
    print(counter, gcounter, 'done')
    return('Finished splitting yo data')
    
if __name__ == '__main__':
    parseprot('../data/tm_alpha.txt')
