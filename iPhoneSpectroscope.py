"""
A program to identfy a gas from its spectrum.
INPUTS: 
        1) the spectral file (assumes the picture is taken with 
        a specific iPhone attachment)

        2) how much smoothing is needed

eg: python3 iPhoneSpectroscope.py LightD_2.tif 50

Prints the peaks (wavelengths in nm) and shows a histogram of the light.

In the folder: txt is a sub-folder with text files for each element.
The first column is wavelength in Angstroms (10 times wavelength in nm).
The second column is intesity.

"""



import sys
sys.path.append('/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python')

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import signal
from ReadElementFile import ReadElementFile   


# ----- FLATTEN ----- #
def flatten(img):
    w, h = img.size
    data = []
    for x in range(w):
        value = 0
        for  y in range(h):
            value = value + img.getpixel((x,y))
        data = data + [value]
    return data


# ----- Find Zero ---- #
def findPeak(data, range_min, range_max):
    if range_max == "all":
        range_max = len(data)

    maximum = 0    # maximum value
    maximum_x = 0  # x position of maximum value
    
    for x in range(range_min, range_max):
        if data[x] > maximum:
            maximum = data[x]
            maximum_x = x
    
    twothirds = maximum * .6667
    bottom = maximum_x
    top = maximum_x

    while data[bottom] > twothirds:
        bottom = bottom - 1
    while data[top] > twothirds:
        top = top + 1

    return int((bottom + top)/2)


# ----- Smoothing ---- #
def smooth(data):
    smooth_data = []
    for x in range(0, len(data)-1):
        smooth_data = smooth_data + [(data[x-1]+2*data[x]+data[x+1])/4]
    return smooth_data


# ----- Find Peaks ----- #
def findPeaks(data):
    peakLambda = []                         # returns the wavelenghts of the peaks
    peakIntensity = []                      # returns the intensities of the peaks     
    for x in range(1, len(data)-1):         # cycle through all the data points
        if data[x-1] < data [x] and data[x+1] < data[x] and data[x] >100:
                                            # if a data point is larger than the data points 
                                            # to its left and right
            peakIntensity = peakIntensity + [int(data[x])]            # adds intensity to its list
            peakLambda = peakLambda + [int((100*x+67140)/197)]  # adds frequency to its list 
    return (peakLambda, peakIntensity)



# ------------------------ #
if __name__ == '__main__':

    elements = ReadElementFile()       # makeDictionary() creates a dictionary of elements
                                        # key = element name
                                        # value = wavelenghts of peaks

    tiff = "tif/" + (sys.argv[1])     # what file are we looking at?
    times = int(sys.argv[2])          # how much should it be smoothed?
    img = Image.open(tiff)            # open the file

    box = (0, 1200, 3264, 1250)       # dimensions of the cropped box
    img = img.crop(box).convert('L')      # crop and convert to grayscale

    data = flatten(img)               # turn into a histogram
    
    zero = findPeak(data, 0, "all")       # find the center

    data = data[zero+500:zero+1250]   # crop the data to visible light 
    
    for x in range(0, times):         #  smooth the data
        data = smooth(data)

    x = [n for n in range(0, len(data))]
                                      # for the raw data
    x = [(100*n+67140)/197 for n in range(len(data))]    
                                      # for wavelength on the x axis
    
    peakLambda, peakIntensity = findPeaks(data)
    print(peakLambda, peakIntensity)
    index = peakIntensity.index(max(peakIntensity))
    maxIntensity = peakIntensity[index]
    maxLambda = peakLambda[index]

#    plt.plot(x,data)                  # make the plot
#    plt.show()                        # show the plot

#    img.show()

