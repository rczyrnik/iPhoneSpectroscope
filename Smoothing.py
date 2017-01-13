"""
To determine optimal smoothing by running the iPhonespectroscope.py
multiple times and graphing the result

"""
import matplotlib.pyplot as plt


from iPhoneSpectroscope import iPhoneSpectroscope
x = []
y = []
for i in range(1, 10):
    peakLambda, peakIntensity = iPhoneSpectroscope(3, i)
    x.append(i)
    y.append(len(peakLambda))

plt.plot(x, y)
plt.show()
