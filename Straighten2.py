"""
the old program was talking too long
"""

import pickle
import sys
from scipy.misc import toimage

if __name__ == "__main__":
    num = str(sys.argv[1])
    filename = "newpic" + num + ".pk1"
    try:
        file = open(filename, 'rb')
        newpic = pickle.load(file)
        file.close()
    except:
        print("No Dice :(")

    im = toimage(newpic)
    im.save("foobar333.png")

