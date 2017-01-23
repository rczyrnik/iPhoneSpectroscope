"""
The pic files are distorted cause optics
I want them straight
"""

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from iPhoneSpectroscope import smooth
from iPhoneSpectroscope import findPeak
from scipy.misc import toimage
import pickle
import sys

def getLine(img, row):
    width, height= img.size
    box = (0, row, width, row+1)
    flatimg = img.crop(box).convert('L')
    line = []
    for x in range(width):
        line = line+[flatimg.getpixel((x,0))]
    return(line)

def newpic(img):
    width, height = img.size
    newwidth = int(width/2)-100
    newpic = []
    for i in range(height):
        line = getLine(img, i)
        center = findPeak(line, 0, "all")
        newline = line[center+60:center+newwidth]
        m = newline.index(max(newline))
        newpic = newpic + [newline] 
    return(newpic)

def savepic(newpic):
    filename = "newpic"+ num + ".pk1"
    output = open(filename, 'wb')
    pickle.dump(newpic, output)
    output.close
    

if __name__=='__main__':

    num = str(sys.argv[1])
    tif = 'tif/Element' + num + '.tif'
    img = Image.open(tif)

    savepic(newpic(img))
