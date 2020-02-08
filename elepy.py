import math
import numpy as np
from matplotlib import pyplot as plt


x = np.arange(10,19.5,0.1)
e = [math.sin(i) for i in x]



def calc_RL(r,l,d):
    pass

def calc_RC(r,c,q):
    i=[0 for i in x]
    vq=[0 for i in x]
    qt=q
    for j, ele in enumerate(e):
        i[j]=(ele-qt)/c/r
        
        vq[j]=qt/c
        before_q=qt
        qt+=i[j]

        if abs(before_q)<abs(ele) and abs(qt)>abs(ele):
            qt=ele*c
           # print(str(j*0.1) +'s  ele*c = '+str(vq[j]))
    
    fig,ax1 = plt.subplots()

    ax1.plot(x,e,color='tab:orange',label='Volt')
    ax2 = ax1.twinx()
    ax2.plot(x,i,color='tab:green',label = 'anpare')
    plt.title('RC')

    #ax3 = ax2.twinx()
    #ax1.plot(x,vq,color='tab:red',label = 'Vc')
    #ax1.legend(loc=0)
    
    plt.show()


def calc_RLC():
    pass

if __name__=='__main__':
    calc_RC(10,0.1,0)




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