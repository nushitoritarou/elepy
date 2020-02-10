import math
import numpy as np
from matplotlib import pyplot as plt


x = np.arange(0,20,0.1)
e = [1 for i in x]



def calc_RL(r,l):
    # 交流でLの値が小さい時変な感じになる
    i=[0 for i in x]
    vl=[0 for i in x]
    dt=0
    for j,ele in enumerate(e):
        i[j]=dt/l
        Vr=r*i[j]
        vl[j]=ele-Vr
        before_d=dt
        dt+=vl[j]
        #print(f'i : {i[j]}   {vl[j]}    {before_d}')
        di=dt
        if abs(before_d)<abs((ele/r)*l) and abs(dt)>abs((ele/r)*l):
            dt=(ele/r)*l
            print(f'{j*0.1}sec ,dt = {dt} , before_d = {before_d} , dt = {di} , ele = {ele}')
            
        
    fig,ax1 = plt.subplots()

    ax1.plot(x,e,color='tab:orange',label='Volt')
    ax2 = ax1.twinx()
    ax2.plot(x,i,color='tab:green',label = 'anpare')
    plt.title('RL')

    plt.show()


def calc_RC(r,c,q):
    # 抵抗とコンデンサの積が0 よりも小さすぎると電流がマイナスに発散することがある
    i=[0 for i in x]
    vq=[0 for i in x]
    qt=q
    for j, ele in enumerate(e):
        i[j]=(ele/r) - (qt/(r*c))
        print(f'i : {i[j]}  {ele/r}  , {qt/(r*c)}')
        vq[j]=qt/c
        before_q=qt
        qt+=i[j]
        qi=qt
        print(f'q : {before_q} , {ele*c} , {qt}')
        if abs(before_q)<=abs(ele*c) and abs(qt)>abs(ele*c):     #今フレームでは貯められた電荷量が 電圧*静電容量を超えてない　かつ　次のフレームではそれを超える　とき
            qt=ele*c
            #print(f'{j*0.1}sec ,qt = {qt} , before_q = {before_q} , qt = {qi} , ele = {ele}')
    
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
    calc_RL(10,100)


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