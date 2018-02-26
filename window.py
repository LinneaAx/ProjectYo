proteinseq = 'MDTCGVGYVALGEAGPVGNMTVVDSPGQEVLNQLDVKTSSEMTSAEASVEMSLPTPLPGFEDSPDQRRLPPEQESLSRLEQPDLSSEMSKVSKPRASKPGRK'

windowz = []
for protseq in proteinseq:
    protseq = ((n)*'0')+protseq+((n)*'0')
    for i in range(0, len(protseq)):
        if i+(ws) > len(protseq):
            break
        temp = protseq[i:i+(ws)]
        protriplets.append(temp)
