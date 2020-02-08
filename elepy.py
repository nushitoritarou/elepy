import math
import numpy as np
from matplotlib import pyplot as plt

def data_plot(x,y,z):
    #fig = plt.figure(figsize=(10,6))
    fig,ax1 = plt.subplots()

    x = np.arange(0,10,0.1)     #?　0-10 を0.1 幅
    y= [math.sin(i) for i in x]
    z= [5*math.cos(i) for i in x]

    ax1.plot(x,y,color='tab:orange')

    ax2 = ax1.twinx()

    ax2.plot(x,z, color='tab:green')
    plt.title('title')
    plt.xlabel('X軸ラベル')
    plt.ylabel('Y軸ラベル')

    plt.show()

if __name__=='__main__':
    data_plot()