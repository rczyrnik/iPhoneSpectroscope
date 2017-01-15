"""
INPUT: tiff file
OUTPUT: spectrum (full width of pic)
"""
import sys
import matplotlib.pyplot as plt
from PIL import Image

def Spectrum(pic):
    tif = "tif/Element"+str(pic)+".tif"
                            # "pic' is a number that identifies the file
                            # this line recreates the full file name
    img = Image.open(tif)
                            # opens the tif file    
    width,height = img.size
                            # gets the size of the tif file
    box = (0, height/2-25, width, height/2+25)
                            # identifies the cropped region
                            # eventually want to find a better step here
    img = img.crop(box).convert('L')
                            # crops and converts to grayscale
    
    data = []
    for x in range(width):
        value = 0
        for y in range(50):
            value = value + img.getpixel((x, y))
        data = data + [value]
    return(data)

if __name__ == '__main__':
    pic = sys.argv[1]
    data = Spectrum(pic)
    plt.plot(data)
    plt.title("Picture " + str(pic))
    plt.savefig("Picture"+str(pic)+".png")
    plt.show()
