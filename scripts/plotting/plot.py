import numpy as np
import matplotlib.pyplot as plt

def plot(file_name):
    with open ('../outputfiles/'+file_name, 'r') as q:
        data = q.read().splitlines()
        data = list(data)
    wstot = []
    scoretot = []
    for lines in data:
        ws = lines[3:5]
        lines = lines.split()    
        score = lines[-1]
        scoretot.append(score)
        wstot.append(ws)
    scoretot = np.array(scoretot)
    wstot = np.array(wstot)
    plt.xlabel('Windowsize')
    plt.ylabel('MCC')
    plt.title('Comparison of MCC for different windowsizes')
    
    plt.plot(wstot, scoretot)
    plt.show()



plot('ws_mcc_results.txt')


    
