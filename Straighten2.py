"""
the old program was talking too long
"""

import pickle
import sys
import numpy
import matplotlib.pyplot as plt
from scipy.misc import toimage
from iPhoneSpectroscope import findPeak

def step1(oldPic):
    peaks = []

    for y in range(len(oldPic)):
        peaks += [findPeak(oldPic[y], 0, "all")]

    la = numpy.polyfit(range(len(peaks)), peaks,2)
    minX = int(-la[1]/(2*la[0]))
    minY = int(la[0]*minX**2 + la[1]*minX + la[2])

    newWidth = int(minY*len(oldPic[1])/max(peaks)-1)

    newPic = []
    for y in range(len(oldPic)):
        oldRow = oldPic[y]
        ratio = (la[0]*y**2+la[1]*y+la[2])/minY
        newRow = []
        for x in range(newWidth):
            newRow += [oldRow[int(x*ratio)]]
        newPic += [newRow]

    im = toimage(newPic)
    im.show()

    data = []
    for y in range(len(newPic[0])):
        sum = 0
        for x in range(len(newPic)):
            sum += newpic[x][y]
        data += [sum]
    plt.plot(data)
    plt.show()


if __name__ == "__main__":
    num = str(sys.argv[1])
    filename = "newpic" + num + ".pk1"

    try:
        file = open(filename, 'rb')
        newpic = pickle.load(file)
        file.close()
    except:
        print("No Dice :(")
    
    step1(newpic)
   

