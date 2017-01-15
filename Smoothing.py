"""
To determine optimal smoothing by running the iPhonespectroscope.py
multiple times and graphing the result

"""
import matplotlib.pyplot as plt
import sys

from iPhoneSpectroscope import iPhoneSpectroscope

def Smoothing(element):
    x = []
    y = []
    for i in range(1, 100):
        peakLambda, peakIntensity = iPhoneSpectroscope(element, i)
        x.append(i)
        y.append(len(peakLambda))
    plt.plot(x, y)
    plt.title("Element "+str(element))
    plt.savefig("Element"+str(element)+".png", bbox_inches='tight')
    plt.clf()

if __name__ == '__main__':
#    Element = sys.argv[1]
    for e in range(1, 9):
        Smoothing(e)
