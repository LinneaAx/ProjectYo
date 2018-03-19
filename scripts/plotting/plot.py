import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
def plot(file_name):
    with open ('../../outputfiles/'+file_name, 'r') as q:
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
    plt.title('Comparison of MCC for different windowsizes using LinearSVC')
    
    plt.plot(wstot, scoretot)
    plt.savefig('../../outputfiles/ws.png')


plot('ws_mcc_results.txt')


    
