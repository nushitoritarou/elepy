import math
import numpy as np
from matplotlib import pyplot as plt

def main():
    fig = plt.figure(figsize=(10,6))

    x = np.arange(0,10,0.1)
    y= [math.sin(i) for i in x]

    plt.plot(x,y)

    plt.show()

if __name__=='__main__':
    main()